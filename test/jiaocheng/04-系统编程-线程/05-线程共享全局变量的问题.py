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
g_num = 0

def test1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---in test1 g_num is %d---"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("---in test2 g_num is %d---"%g_num)


t = Thread(target=test1)
t.start()

#time.sleep(3)

t1 = Thread(target=test2)
t1.start()
print("---g_num=%d---"%g_num)

#当没有sleep的时候，2个线程同时在一个CPU上执行，那么就服从系统的进程管理，g_num+=1的执行是分2个步骤的，
#即g_num = g_num + 1，先执行右边的运算，再给左边赋值。当2个线程同时执行时，可能出现刚执行完右边的运算，
#就被系统搁置，转而执行另一个线程，执行完另一个线程时，回来在执行搁置的线程，这样就会出现问题。如果中间
#sleep 1s的话，等上一个进程执行完，再执行另一个进程，那么就不会出现问题了。

