#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 06:02:07 PM CST

# File Name: 14-对有返回值的函数进行装饰.py
# Description:

"""
#比如做了一个加法的函数，后面有用装饰器加了些判断的功能
def charge(func):
    def inner(*args):
        for i in args:
            if i<0:
                print("%d是负数，不想计算" %i)
        x = func(*args)  #x保存返回的值
        return x #把返回值再返回给25行出的调用
    return inner

@charge
def sumnum(a,b):
    print("计算%d + %d"%(a,b))
    return a+b

sum = sumnum(-11,22)
print("结果是..%d" %sum)
