#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 01 Apr 2018 03:26:32 PM CST

# File Name: 02-tcp客户端.py
# Description:

"""

from socket import AF_INET, SOCK_STREAM, socket

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('127.0.0.1', 7788))
while True:
    sendData = input(">")
    if sendData == 'quit':
        break
    client_socket.send(sendData.encode('utf-8'))
    recv_data = client_socket.recv(2048)
    print("recv_data: %s"%recv_data)

client_socket.close()
