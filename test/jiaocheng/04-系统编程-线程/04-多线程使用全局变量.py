#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 02:31:45 PM CST

# File Name: 04-多线程使用全局变量.py
# Description:

"""

from threading import Thread
import time
#线程之间共享全局变量，进程之间是不共享的
g_num = 100

def test1():
    global g_num
    for i in range(3):
        g_num += 1

    print("---in test1 g_num is %d---"%g_num)

def test2():
    global g_num
    print("---in test2 g_num is %d---"%g_num)


print("---start g_num is %d---"%g_num)
t = Thread(target=test1)
t.start()

#延迟一段时间，等待test1的线程执行完成
time.sleep(1)

t1 = Thread(target=test2)
t1.start()


