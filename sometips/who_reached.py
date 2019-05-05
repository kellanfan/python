#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 08 Mar 2019 09:31:18 AM CST

# File Name: netmask-counter.py
# Description:

"""
import sys
from IPy import IP
from pings import Ping

ip = input('请输入ip信息<10.1.1.0/24>: ')

try:
    IP(ip).net()
    IP(ip).netmask()
except:
    print("您输入的ip地址不合法，请重新输入！")
    sys.exit()

mypings = Ping(timeout=3)
for i in IP(ip):
    if mypings.ping(str(i)).is_reached():
        print("%s is reached.."%i)
    else:
        print("%s cannot reached.."%i)
