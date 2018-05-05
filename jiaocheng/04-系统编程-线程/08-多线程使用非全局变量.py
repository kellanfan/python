#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 04:52:14 PM CST

# File Name: 08-多线程使用非全局变量.py
# Description:

"""

from threading import Thread
import threading
import time
#非全局变量不共享，不用加锁,线程内的函数中的变量，不共享，各自是各自的
def test1():
    name = threading.current_thread().name
    print("---thread name is %s---"%name)
    num = 100
    if name == 'Thread-1':
        num += 1
    else:
        time.sleep(2)
    print("---thread is %s,num is %d"%(name,num))

t1 = Thread(target=test1)
t1.start()
t2 = Thread(target=test1)
t2.start()
