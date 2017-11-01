#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 30 Oct 2017 07:54:28 PM CST

# File Name: 15-del方法.py
# Description:

"""
import sys

class Dog:
    def __del__(self): #当引用个数为0时，执行
        print "=====del======="

dog1 = Dog() #变量dog1指向对象Dog
print sys.getrefcount(dog1) #获取对象当前的引用个数,输出的个数会比引用个数多1
dog2 = dog1  #变量dog2也指向对象Dog
print sys.getrefcount(dog1) #获取对象当前的引用个数

del dog2 #删除对象
print sys.getrefcount(dog1) #获取对象当前的引用个数
del dog1
