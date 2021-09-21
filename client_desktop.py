from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from layout import Ui_MainWindow
import sys
from PyQt5 import sip
import os
import socket

CMD=''
wifiModuleIp=''
wifiModulePort=0
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

def getIpAndPort():
    global wifiModuleIp
    global wifiModulePort
    global connected
    values = ui.textEdit.toPlainText()
    print('Ip and port string: ',values)
    temp = values.split(':')
    wifiModuleIp = temp[0]
    wifiModulePort = (int)(temp[1])
    print('IP: ',wifiModuleIp)
    print('PORT: ',wifiModulePort)
    
def btnUpClicked():
    getIpAndPort()
    global CMD
    global socket
    global connected
    if not connected:
        setConnection()
    CMD = 'Up'
    socket.send(str.encode(CMD))
    print('UP')
    
def btnDownClicked():
    getIpAndPort()
    global CMD
    global socket
    if not connected:
        setConnection()
    CMD = 'Down'
    socket.send(str.encode(CMD))
    print('DOWN')
    
def setConnection():
    global wifiModuleIp
    global wifiModulePort
    global connected
    socket.connect((wifiModuleIp,wifiModulePort))
    connected=True
        
        
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButtonUp.clicked.connect(btnUpClicked)
    ui.pushButtonDown.clicked.connect(btnDownClicked)
    
    sys.exit(app.exec_())
