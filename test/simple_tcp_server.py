#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 13 Mar 2019 06:40:54 PM CST

# File Name: simple_udp_server.py
# Description:

"""
import time
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if self.data == b'time':
            recv = "now time is: " + time.ctime()
            self.request.sendall(recv.encode())
        else:    
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "", 21567

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
