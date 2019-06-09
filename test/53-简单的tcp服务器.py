# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   simple_tcp_server.py
@Time    :   2019/06/09 08:39:57
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

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
