#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 07:49:33 PM CST

# File Name: 01-线程.py
# Description:

"""

from threading import Thread
import time
#如果多个线程执行同一个函数的话，格子之间不会有影响
def test():
    print("---aaaa---")
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()
