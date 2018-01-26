#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 05:33:11 PM CST

# File Name: 12-对有参数的函数进行装饰.py
# Description:

"""
def func(func):
    def inner(*args, **kwargs): #为了解决不定长的问题，使用不定长参数
        print("---innner----")
        func(*args, **kwargs)  
    return inner

@func
def test(a, b): 
    print("---test--%d---%d" %(a,b))

@func
def test1(a, b, c, d): 
    print("---test--%d---%d---%d---%d" %(a,b,c,d))
test(1,2)
test1(1,2,3,4)
