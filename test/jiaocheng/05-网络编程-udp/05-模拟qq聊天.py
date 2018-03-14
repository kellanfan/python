#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 14 Mar 2018 02:33:38 PM CST

# File Name: 05-模拟qq聊天.py
# Description:

"""
from socket import *
from threading import Thread
from time import ctime


def recvMsg():
    while True:
        content,info = udpSocket.recvfrom(1024)
        print('\r') #清空之前的<<
        print(">>[%s]#%s:%s"%(ctime(),info[0],content.decode('utf-8')))
        print("<<") #重新输出<<

def sendMsg():
    while True:
        content = input("<<")
        udpSocket.sendto(content.encode('utf-8'), (destIp, destPort))

#定义全局变量
udpSocket = None
destIp = ""
destPort = 0

def main():
    #global化变量
    global udpSocket
    global destIp
    global destPort
    #创建socket,绑定ip和端口
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    bindinfo = ('',7789)
    udpSocket.bind(bindinfo)
    #输入目标信息
    destIp = input("请输入目标ip：")
    destPort = int(input("请输入目标port："))
    #创建2个线程
    t_recv = Thread(target=recvMsg)
    t_send = Thread(target=sendMsg)
    #启动2个线程
    t_recv.start()
    t_send.start()
    #主进程阻塞
    t_recv.join()
    t_send.join()
    #关闭socket
    s.close()

if __name__ == '__main__':
    main()

