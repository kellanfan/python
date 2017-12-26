#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 08:14:41 PM CST

# File Name: 06-tsTclientSS.py
# Description:

"""

#from SocketServer import (TCPServer as TCP,
#             StreamRequestHandler as SRH)
from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
