#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 26 Dec 2017 10:25:25 AM CST

# File Name: 07-myFTPServer.py
# Description: 模拟FTP服务

"""
from socket import *
from time import ctime

HOST = '' #为空，表示可以使用任何可用地址
PORT = 21567
BUFSIZE = 10240
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5) #传入连接请求的最大数

f = open('ftp.data','w')
while True:
    print "waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "Connected from: " , addr
    try:
        while True:
            data = tcpCliSock.recv(BUFSIZE) + '\n'
            if not data: #如果消息是空白的说明客户退出，跳出对话循环
                break
            f.write(data)
            tcpCliSock.send('[%s] date write ok' %ctime())
    except:
        tcpCliSock.close()
        print "connection exit..."
f.close()
tcpSerSock.close()
