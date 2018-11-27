#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 27 Nov 2018 01:52:20 PM CST

# File Name: myzktest.py
# Description:

"""

import zookeeper

def myWatch(zk,type,state,path):
    print "zk:",str(type),str(state),str(path)
    zookeeper.get(zk,path,myWatch)

zk = zookeeper.init("localhost:2181")
data=zookeeper.get(zk,"/zk-bbb",myWatch)
print data
