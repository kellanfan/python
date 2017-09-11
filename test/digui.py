#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Mon 11 Sep 2017 07:58:03 PM CST

# File Name: digui.py
# Description: 递归，就是自己调用自己，但是一定要注意什么时候结束调用，否则就是一个死循环，最终导致内存溢出，从而程序崩溃

"""
#4! = 4*3*2*1

def normal_digui(num):
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result

def digui(num):
    if num > 1:
        return num * digui(num-1)
    else: #判断何时结束调用返回值
        return num

'''
下面这个就是死循环
def printaa():
    print "aaa"
    printaa()

printaa()
'''
print normal_digui(4)
print digui(4)
