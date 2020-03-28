# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   17-etcd的leader选举.py
@Time    :   2020/03/26 11:42:39
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import etcd
import socket
import time

class EtcdWatcher(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect()
        self.hostname = socket.gethostname()
        self.path = '/cluster/leader'
        self.ttl = 60

    def connect(self):
        try:
            self.client = etcd.Client(host=self.host, port=self.port)
            self.client.version
        except Exception as e:
            print('ERROR: Connect to Etcd server failed: [{}]'.format(e))

if __name__ == "__main__":
    a = EtcdWatcher('192.168.1.4',2379)