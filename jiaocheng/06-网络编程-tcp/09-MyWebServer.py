#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 20 Apr 2018 09:49:17 AM CST

# File Name: 09-MyWebServer.py
# Description: 主要实现了web服务器和框架的结合

"""

from socket import *
from multiprocessing import Process
import time
import os
import sys
import re

ROOT_DIR = os.getcwd()
WSGI_PYTHON_DIR = './wsgi'

class HTTPserver(object):
    '''server class'''
    def __init__(self, application):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.app = application
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
        env = {
            "PATH_INFO": request_file,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + '\r\n' + response_body

        client_socket.send(bytes(response, 'utf-8'))
        client_socket.close()

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR) #添加wsgi脚本目录，以便加载脚本模块
    #框架名以参数传给server，这样server可以兼容各种框架
    if len(sys.argv) < 2:
        sys.exit("python3 MyWebServer.py MYWebFrameWork:app")
    frame_name, app_name = sys.argv[1].split(':')
    m = __import__(frame_name) #加载框架模块
    app = getattr(m, app_name)
    httpserver = HTTPserver(app)
    httpserver.bind(8899)
    httpserver.start()
    httpserver.close()

if __name__ == '__main__':
    main()
