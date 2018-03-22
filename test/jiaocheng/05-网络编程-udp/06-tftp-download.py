#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 22 Mar 2018 09:00:48 PM CST

# File Name: 03-tftp_download.py
# Description:

"""

import struct
from socket import *
import sys

#判断参数个数是否是2，是2的话，将serverip定好
if len(sys.argv) != 3: #脚本名也算一个参数
    print "="*30
    print "Usage:"
    print "     python xx.py ip file"
    print "="*30
    sys.exit(-1)
else:
    server_ip = sys.argv[1]
    download_file = sys.argv[2]

print server_ip, download_file
#创建socket
udp_socket = socket(AF_INET, SOCK_DGRAM)
#创建请求数据
request_data = struct.pack('!H%dsb5sb'%len(download_file),1,download_file,0,'octet',0)
#发送请求数据
udp_socket.sendto(request_data, (server_ip, 69))
#num记录上一个包的序号
num = 0
flag = True
f = open(download_file,'w')
while True:
    #接收发送的数据
    recvData, recvInfo = udp_socket.recvfrom(1024)
    #根据tftp协议，解包将相关信息取出
    action_num = struct.unpack('!H',recvData[:2])
    packet_num = struct.unpack('!H',recvData[2:4])
    #如果是数据包
    if action_num[0] == 3:
        num += 1 #加1就表明应该接收到的是这个序号的包才是对的
        #如果数据很大，包的序号超过了2^32，那么需要重新计数
        if num == 65536:
            num = 0

        if num == packet_num[0]:
            f.write(recvData[4:])
            num = packet_num[0] #将值定成现在的包序号

        #发送ack包,4是action，数据是包序号
        ackData = struct.pack('!HH',4,packet_num[0])
        udp_socket.sendto(ackData, recvInfo)

    elif action_nump[0] == 5:
        print "错误..文件不存在!"
        flag = False
        break

    if len(recvData) < 516:
        break

if flag == True:
    f.close()
else:
    sys.unlink(download_file)

udp_socket.close()
