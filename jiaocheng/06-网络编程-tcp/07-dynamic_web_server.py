#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 11 Apr 2018 02:30:55 PM CST

# File Name: 07-dynamic_web_server_class.py
# Description:

"""
from socket import socket,AF_INET,SOCK_STREAM
from multiprocessing import Process
import time
import os
import sys
import re

ROOT_DIR = os.getcwd()
WSGI_PYTHON_DIR = './wsgi'

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

    def start_response(self,status, headers):
        '''构建新的请求头'''
        response_headers = 'HTTP1.1 %s OK\r\n'%status
        #将特殊添加的请求头参数加到headers中
        for header in headers:   
            response_headers += "%s: %s\r\n"%header
        #直接将response_headers定义成class的属性
        self.response_headers = response_headers

    def clientdeal(self, client_socket, client_info):
        client_data = client_socket.recv(2048).decode('utf-8')
        datalist = client_data.splitlines()
        request_start_line = datalist[0]
        request_file = re.match(r"\w+ +(/[^ ]*) ", request_start_line).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", request_start_line).group(1)

        print("%s %s request_action: %s, request_file: %s"
                            %(time.ctime(),str(client_info), method, request_file))
        
        #判断，如果没有写具体文件，那么直接返回index.html内容

        if request_file.endswith('.py'):
            env = {
                'PATH_INFO': request_file,
                'METHOD': method
            } #这个应该是上面接收到数据带的参数，目前先传个空
            try:
                mod = __import__(request_file[1:-3]) #截取脚本名
            except:
                recv_data = 'HTTP1.1 404 Not Found\r\nServer: My server\r\nNot Found!!!\n'
            else:
                response_body = mod.application(env, self.start_response)
                recv_data = self.response_headers + '\r\n' + response_body
        else:
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
                
        client_socket.send(bytes(recv_data, 'utf-8'))
        client_socket.close()

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR) #添加wsgi脚本目录，以便加载脚本模块
    httpserver = HTTPserver()
    httpserver.bind(8899)
    httpserver.start()
    httpserver.close()

if __name__ == '__main__':
    main()
