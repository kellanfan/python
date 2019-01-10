#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 01:50:28 PM CST

# File Name: 01-tsTserv.py
# Description: TCP服务端

"""

from socket import *
from time import ctime

HOST = '' #为空，表示可以使用任何可用地址
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5) #传入连接请求的最大数

while True:
    print "waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "Connected from: " , addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data: #如果消息是空白的说明客户退出，跳出对话循环
            break
        tcpCliSock.send('[%s] %s' %(ctime(), data))
    tcpCliSock.close()
tcpSerSock.close()
