#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 05 Apr 2018 08:19:40 PM CST

# File Name: 04-static_web_server.py
# Description: 实现静态网站服务器，只是简单的回复静态内容

"""

from socket import *
from multiprocessing import Process
import time

#创建socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("",8899))
server_socket.listen(10)

def clientdeal(client_socket, client_info):
    client_data = client_socket.recv(2048).decode('utf-8')
    datalist = client_data.split()
    day = time.ctime()
    print("%s###%s----request_action: %s, request_path: %s, Http_version: %s"
            %(day,str(client_info),datalist[0],datalist[1],datalist[2]))
    response_start_line = 'HTTP1.1 200 OK\r\n'
    response_headers = 'Server: Kellan server'
    response_body  = 'Fankai is The best one!!!'
    response = response_start_line + response_headers + '\r\n' + response_body
    client_socket.send(bytes(response, 'utf-8'))
    client_socket.close()
    
def main():
    while True:
        client_socket, client_info = server_socket.accept()
        p = Process(target=clientdeal, args=(client_socket, client_info))
        p.start()
    p.close()
    server_socket.close()

if __name__ == '__main__':
    main()
