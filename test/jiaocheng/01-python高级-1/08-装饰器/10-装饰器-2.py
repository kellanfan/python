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
#只要解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用的时候才装饰
@w1   #等价于f1=w1(f1)   
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")
#调用之前已经装饰了
f1() #对f1的调用不改变
f2()
