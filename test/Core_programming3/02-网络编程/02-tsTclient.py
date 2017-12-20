#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 02:03:22 PM CST

# File Name: 02-tsTclient.py
# Description:

"""

from socket import *

HOST = 'localhost'  #服务器的主机和端口
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM) #创建套接字
tcpCliSock.connect(ADDR) #连接服务端

while True: #进入循环
    data = raw_input('> ') #手动输入数据
    if not data: #没有数据则退出
        break
    tcpCliSock.send(data) #将输入的数据发送给服务端
    data = tcpCliSock.recv(BUFSIZE) #接收数据
    if not data:
        break
    print data

tcpCliSock.close()
