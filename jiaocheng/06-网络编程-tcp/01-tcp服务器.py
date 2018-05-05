#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 01 Apr 2018 02:55:51 PM CST

# File Name: 01-tcp服务器.py
# Description:

"""

from socket import *
#创建server的套接字
server_socket = socket(AF_INET, SOCK_STREAM)
#绑定
server_socket.bind(("",8899))
#监听，使socket成为被动接收，里面的5的意思是连接数
server_socket.listen(5)
#server的套接字负责接收，返回的是一个新的socket以及客户端的信息
#把server的socket空出来接收新的链接
client_socket, client_info = server_socket.accept()
#连接成功后，新的socket来接收client发过来的数据
client_data = client_socket.recv(1024)

print("%s:%s"%(str(client_info),client_data))
#关闭socket
client_socket.close()
server_socket.close()
