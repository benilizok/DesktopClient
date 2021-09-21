from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(800, 300)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background-color: rgb(199, 199, 199);\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"background-color: rgb(199, 199, 199);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        # label for textfield
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 150, 40))
        self.label.setObjectName("label")
        # text field for typing ip and port
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 50, 400, 40))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.textEdit.setObjectName("textEdit")
        # up button
        self.pushButtonUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUp.setGeometry(QtCore.QRect(300, 150, 100, 30))
        self.pushButtonUp.setObjectName("buttonUp")
        self.pushButtonUp.setStyleSheet("background-color: rgb(73, 182, 174)")
        # down button
        self.pushButtonDown = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDown.setGeometry(QtCore.QRect(500, 150, 100, 30))
        self.pushButtonDown.setObjectName("buttonDown")
        self.pushButtonDown.setStyleSheet("background-color: rgb(73, 182, 174)")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Servo controller"))
        self.pushButtonUp.setText(_translate("MainWindow", "Up"))
        self.pushButtonDown.setText(_translate("MainWindow", "Down"))
        self.textEdit.setText(_translate("MainWindow", "198.168.43.193:21567"))
        self.label.setText(_translate("MainWindow", "Input host and port"))
        
