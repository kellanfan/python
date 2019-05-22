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
from multiprocessing import Pool

def ping_target(ip):
    mypings = Ping(timeout=3)
    if mypings.ping(str(ip)).is_reached():
        print("%s is reached.."%ip)
    else:
        print("%s cannot reached.."%ip)

if __name__ == '__main__':
    ip_network = input('请输入ip信息<10.1.1.0/24>: ')
    try:
        IP(ip_network).net()
        IP(ip_network).netmask()
    except:
        print("您输入的ip地址不合法，请重新输入！")
        sys.exit()
    p = Pool(10)
    for i in IP(ip_network):
        p.apply_async(ping_target, (i,))
    p.close()
    p.join()