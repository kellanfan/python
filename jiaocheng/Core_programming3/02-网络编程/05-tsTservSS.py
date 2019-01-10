#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Dec 2017 08:02:18 PM CST

# File Name: 05-tsTservSS.py
# Description:

"""
from SocketServer import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH): #创建一个子类
    def handle(self): #重写handle方法
        print "connected from: ", self.client_address
        #将输入输出套接字看做类似文件的对象，使用readline获取客户端信息，write将字符串发送回客户端
        self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline())) 

tcpServ = TCP(ADDR, MyRequestHandler) #创建TCP服务器
print "waiting for connection..."
tcpServ.serve_forever() #无限运行

