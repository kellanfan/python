#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 10:14:54 AM CST

# File Name: 01-fork.py
# Description:

"""

import os
import time
try:
    ret = os.fork()
    print(ret) #父进程中fork的返回值，就是刚刚创建出来的子进程的pid
    if ret == 0:
        while True:
            print("curr pid is %d and ppid is %d" %(os.getpid(),os.getppid()))
            time.sleep(1)
    else:
        while True:
            print("curr pid is %d and ppid is %d" %(os.getpid(),os.getppid()))
            time.sleep(1)
except:
    print("byebye...")
