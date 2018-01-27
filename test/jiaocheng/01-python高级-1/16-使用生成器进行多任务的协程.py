#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 27 Jan 2018 04:34:59 PM CST

# File Name: 16-使用生成器进行多任务的协程.py
# Description:

"""

def test1():
    while True:
        print('----1----')
        yield None

def test2():
    while True:
        print('----2----')
        yield None

a = test1()
b = test2()
while True:
    a.__next__()
    b.__next__()
