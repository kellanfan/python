#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Jun 2018 08:20:03 PM CST

# File Name: io_moniter.py
# Description:

"""

import os

def check_io():
    f = open('/pitrix/bin/.curr_status_io_rate','w')
    cmd = "iotop -P -b -n 1 -o |awk '{print $1,$10}'|grep ^[0-9]"
    temp = os.popen(cmd).read()
    if temp:
        l_temp = filter(None,temp.split('\n'))
        for line in l_temp:
            pid = line.split()[0]
            io_rate = line.split()[1].split('.')[0]
#if int(io_rate) > 50:
            msg = "pid %s iorate: %s"%(pid, io_rate)
            f.write(msg)
    f.close()

if __name__ == '__main__':
    check_io()

