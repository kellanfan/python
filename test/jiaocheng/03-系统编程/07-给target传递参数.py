#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 04:05:00 PM CST

# File Name: 07-给target传递参数.py
# Description:

"""

from multiprocessing import Process
import os

def test(num):
    print("pid=%d,ppid=%d,,,,num=%d"%(os.getpid(), os.getppid(), num))


p = Process(target=test, args=(100,))
p.start()
print("----main--pid=%d--"%os.getpid())
