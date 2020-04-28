from PyQt5 import QtCore, QtGui, QtWidgets

STYLE_SHEET = """
QWidget{
    background-color: blue;
}
QLabel {
    font: medium Ubuntu;
    font-size: 20px;
    color: #006325;
}

QVBoxLayout {
    background-color: #006325;
    color: white;

    min-width:  70px;
    max-width:  70px;
    min-height: 70px;
    max-height: 70px;

    border-radius: 35px;
    border-width: 1px;
    border-color: #ae32a0;
    border-style: solid;
}
QPushButton:hover {
    background-color: #328930;
}
QPushButton:pressed {
    background-color: #80c342;
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputLabel.setFont(font)
        self.inputLabel.setObjectName("inputLabel")
        self.horizontalLayout.addWidget(self.inputLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.verticalLayout.addWidget(self.resultLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.menubar.setStyleSheet("""
        QMenuBar {
             background-color: blue;
        }
        """)
        self.inputLabel.setText(_translate("MainWindow", "Имя игрока: "))
        self.pushButton.setText(_translate("MainWindow", "OK"))
