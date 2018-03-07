#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 02:55:07 PM CST

# File Name: 06-列表传递给线程.py
# Description:

"""
#通过将列表以参数的形式，线程之间也是可以共享的
from threading import Thread
import time

def test1(num):
    num.append(66)
    print("---in test1---",num)

def test2(num):
    time.sleep(1)
    print("---in test2---",num)

g_num = [11,22,33]

t1 = Thread(target=test1,args=(g_num,))
t1.start()

t2 = Thread(target=test2,args=(g_num,))
t2.start()

