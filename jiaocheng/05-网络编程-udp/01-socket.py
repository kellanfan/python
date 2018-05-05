#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 13 Mar 2018 08:06:11 PM CST

# File Name: 01-socket.py
# Description:

"""

from socket import *

#创建socket对象，使用udp，tcp的话是SOCK_STREAM
s = socket(AF_INET, SOCK_DGRAM)

#定义目标的ip和端口
sendtarget = ('127.0.0.1',7788)
while True:
#输入发送的内容
    sendtent = input("请输入：")
#发送
    s.sendto(sendtent.encode('utf-8'), sendtarget) #加编码格式，否则接收端可能会乱码
s.close()
