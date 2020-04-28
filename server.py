import socket
import threading
import json
import game
import sys
from game import Send

BUFFER_SIZE = 2**10

class Server:

    def __init__(self):
        self.clients = [] #массив клиентов
        self.cities = [] #массив городов
        self.last_letter = ""
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9095
        self.quit = True

    def receive(self, client):
        buffer = ""
        while not buffer.endswith(game.END_CHARACTER):
            buffer += client.recv(BUFFER_SIZE).decode(game.TARGET_ENCODING) #получаем сообщение от клиента
        print(buffer)
        return buffer[:-1]

    def connect(self, client):
        while True:
            try:
                send = Send(**json.loads(self.receive(client))) #загрузка данных в json
                if self.last_letter == "" and len(send.city) != 0:
                    self.last_letter = send.city[-1]
            except Exception:
                print("Error")
                return
            if not send.q:
                client.close()
                self.clients.remove(client)
                if len(self.clients) == 1:
                    send.answer = True
                    self.clients[0].sendall(send.marshal())
                    return
                return
            self.broadcast(send, client)


    def broadcast(self, send, client): #метод отправки сообщений клиентам
        if len(self.clients) == 1:
            client.sendall(send.marshal())
            return
        for cl in self.clients:
            if cl != client:
                self.game_logic(send, client, cl)

    def check(self, send): #проверка на правильность города
        if len(self.cities) == 0:
            return True
        if send.city[0].lower() != self.last_letter.lower():
            return False
        for c in self.cities:
            if send.city.lower() == c.lower():
                return False
        return True


    def game_logic(self, send, client1, client2):
        if self.last_letter == "":
            send.start = True
            send.move = True
            client2.sendall(send.marshal())
            send.move = False
            client1.sendall(send.marshal())
            return
        if self.check(send):
            if send.city[-1].lower() == 'ь':
                self.last_letter = send.city[-2]
            else:
                self.last_letter = send.city[-1]
            self.cities.append(send.city)
            send.move = True
            client2.sendall(send.marshal())
            send.move = False
            client1.sendall(send.marshal())
        else:
            send.q = False
            send.answer = True
            client2.sendall(send.marshal())
            send.answer = False
            client1.sendall(send.marshal())
            self.serverClose()

    def run(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen(1)
        while True:
            try:
                client, addr = self.serversocket.accept()
            except Exception:
                print("No connect")
                return
            print(addr, " Подключился")
            self.clients.append(client)
            threading.Thread(target=self.connect, args=(client, )).start()

    def serverClose(self):
        for c in self.clients:
            c.close()
        self.serversocket.close()
        sys.exit()

if __name__ == '__main__':
    Server().run()
