#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 01 Apr 2018 04:49:38 PM CST

# File Name: 03-多任务服务端.py
# Description:

"""

from socket import *
from multiprocessing import Process
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",7788))
serverSocket.listen(10)

def clientdeal(clientSocket,clientInfo):
    while True:
        clientData = clientSocket.recv(2048).decode('utf-8')
        if len(clientData) > 0:
            print("pid: %d ## %s: %s"%(os.getpid(),str(clientInfo),clientData))
        else:
            break

        clientSocket.send("haha".encode('utf-8'))
    clientSocket.close()

while True:
    clientSocket, clientInfo = serverSocket.accept()
    p = Process(target=clientdeal, args=(clientSocket,clientInfo))
    p.start()

p.close()
serverSocket.close()
