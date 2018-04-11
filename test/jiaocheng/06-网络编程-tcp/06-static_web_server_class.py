#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 11 Apr 2018 02:30:55 PM CST

# File Name: 06-static_web_server_class.py
# Description:

"""
from socket import *
from multiprocessing import Process
import time
import os

class HTTPserver(object):
    '''server class'''
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        
    def bind(self, port):
        self.server_socket.bind(("",port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            #client_socket, client_info是局部变量，不需要使用self
            client_socket, client_info = self.server_socket.accept()
            p = Process(target=self.clientdeal, args=(client_socket, client_info))
            p.start()
            client_socket.close()
    
    def close(self):
        self.server_socket.close()

    def clientdeal(self, client_socket, client_info):
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
        try:
            f = open(file_name)
            recv_data = 'HTTP1.1 200 OK\r\nServer: My server\r\n' + f.read()
            f.close()
        except:
            recv_data = 'HTTP1.1 404 Not Found\r\nServer: My server\r\nNot Found!!!\n'
        finally:
            client_socket.send(bytes(recv_data, 'utf-8'))
            client_socket.close()

def main():
    httpserver = HTTPserver()
    httpserver.bind(8899)
    httpserver.start()
    httpserver.close()

if __name__ == '__main__':
    main()
