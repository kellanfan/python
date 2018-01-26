#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 24 Jan 2018 11:03:38 AM CST

# File Name: 10-装饰器-1.py
# Description:

"""

def w1(func): #闭包
    def inner():
        print("---内部函数---")
        func()
    return inner

def f1():
    print("---f1---")

def f2():
    print("---f2---")

f1 = w1(f1)
f1() #对f1的调用不改变
