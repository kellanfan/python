#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 01 Apr 2018 01:54:58 PM CST

# File Name: 07-发送广播.py
# Description:

"""

from socket import *
import sys

#dest = ('10.91.19.255',7788)
dest = ('<broadcast>',7788) #这么写更通用
#创建套接字
s = socket(AF_INET, SOCK_DGRAM)
#对这个需要发送广播的数据的套接字进行修改设置,否则不能发送广播数据
#格式是固定的
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#以广播的形式发送数据到本网络的所有机器上
s.sendto("Hi",dest)
print "等待对方回复..."
while True:
    (ret, addr) = s.recvfrom(2048)
    print "recvived from %s: %s"%(addr, ret)

