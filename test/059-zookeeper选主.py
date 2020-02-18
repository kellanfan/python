# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   059-zookeeper选主.py
@Time    :   2020/02/18 13:43:37
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import socket
import time
from kazoo.client import KazooClient
from kazoo.client import DataWatch
class ZKMaster(object):
    def __init__(self,hosts):
        self.path = "/master"
        self.hostname = socket.gethostname()
        self.zk = KazooClient(hosts=hosts)
        self.zk.start(timeout=5)
        self.is_master = False

    def create_instance(self):
        value = bytes(self.hostname, encoding = "utf-8")
        self.zk.create(path=self.path,value=value,ephemeral=True)

    def data_change(self, data, event):
        if not event:
            print("Nothing to do..")
        if data is not None:
            data = str(data,encoding = "utf-8")
            if data == self.hostname:
                print("I am the master..")
            else:
                print("The current master is [{}], so i will be a slaver..".format(data))
        else:
            try:
                print("Now the master is None, try to be master..")
                self.create_instance()
                self.is_master = True
                print("I am be master!")
            except:
                print("Try to be master failed!")

    def watcher(self):
        try:
            DataWatch(client=self.zk, path=self.path,func=self.data_change)
        except Exception as e:
            print("Create children wather failed: [{}]".format(e))

def run():
    hosts = ['192.168.1.5:2181','192.168.1.6:2181','192.168.1.7:2181']
    try:
        zkc = ZKMaster(hosts)
        zkc.watcher()
        while True:
            print("watching current node data changes..")
            time.sleep(5)
    except Exception as e:
        print("Error: [{}]".format(e))

if __name__ == "__main__":
    run()