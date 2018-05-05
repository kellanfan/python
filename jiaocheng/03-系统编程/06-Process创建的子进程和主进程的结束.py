#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 03:49:13 PM CST

# File Name: 05-Process创建进程.py
# Description:

"""

from multiprocessing import Process
import time

def test():
    for i in range(5):
        print("test--%d-"%i)
        time.sleep(1)

p = Process(target=test)
p.start() #让这个进程开始执行test函数里的代码

#Process的父进程要等所有子进程结束，父进程才结束

