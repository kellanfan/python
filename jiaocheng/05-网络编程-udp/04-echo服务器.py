#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 14 Mar 2018 02:15:15 PM CST

# File Name: 04-echo服务器.py
# Description:

"""

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

bindAddr = ('',7788)
s.bind(bindAddr)

num = 0
while True:
    #接收发送方的信息
    recvcontent = s.recvfrom(1024) 
    #将发送方的信息再发回去
    s.sendto(recvcontent[0], recvcontent[1])
    print("已经将从%s接收到的第%d个数据信息返回给对方,内容为%s"%(recvcontent[1][0],num,recvcontent[0].decode('utf-8')))
    num += 1

s.close()
