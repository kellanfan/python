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
import os


def clientdeal(client_socket, client_info):
    client_data = client_socket.recv(2048).decode('utf-8')
    datalist = client_data.split()
    print("%s %s request_action: %s, request_file: %s, Http_version: %s"
            %(time.ctime(),str(client_info), datalist[0],datalist[1],datalist[2]))
    request_file = datalist[1]
    ROOT_DIR = os.getcwd()
    if request_file == '/':
        file_name = ROOT_DIR + '/index.html'
    else:
        file_name = ROOT_DIR + request_file
    print(file_name)
    try:
#这里需要注意一点，具体是怎么读取，r还是rb，因为linux，unix，mac换行符都是\n，但是windows是\r\n，
#在window系统中，当二进制写入时，需要二进制读取，否则会自动将\n转为\r\n
        f = open(file_name)
        recv_data = 'HTTP1.1 200 OK\r\nServer: My server\r\n' + f.read()
        f.close()
    except:
        recv_data = 'HTTP1.1 404 Not Found\r\nServer: My server\r\nNot Found!!!\n'
    finally:
        client_socket.send(bytes(recv_data, 'utf-8'))
        client_socket.close()
    
def main():
    #创建socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    #server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("",8899))
    server_socket.listen(128)
    while True:
        client_socket, client_info = server_socket.accept()
        p = Process(target=clientdeal, args=(client_socket, client_info))
        p.start()
        client_socket.close() #在主进程中将新创建的socket关闭，否则客户端访问的话会一直卡住
    p.close()
    server_socket.close()

if __name__ == '__main__':
    main()
