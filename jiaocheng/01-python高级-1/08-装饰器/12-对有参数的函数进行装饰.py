#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 05:33:11 PM CST

# File Name: 12-对有参数的函数进行装饰.py
# Description:

"""
def func(func):
    def inner(a, b): #如果a，b没有定义，那么会导致21行的调用失败
        print("---innner----")
        func(a,b)  #如果没有把a，b当做实参进行传递，那么会导致调用18行的函数失败
    return inner

@func
def test(a, b): 
    print("---test--%s---%s" %(a,b))

test('aaa','bbb')
