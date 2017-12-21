#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 07:46:14 PM CST

# File Name: 04-tsUclient.py
# Description:

"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break

    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data
udpCliSock.close()

