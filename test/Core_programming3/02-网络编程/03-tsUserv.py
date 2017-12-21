#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 07:39:09 PM CST

# File Name: 03-tsUserv.py
# Description:

"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print "waiting for connection..."
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s' %(ctime(), data),addr)
    print "received from and returned to: ", addr

udpSerSock.close()
