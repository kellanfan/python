#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 18 Jan 2018 07:52:29 PM CST

# File Name: 04-深拷贝和浅拷贝.py
# Description:

"""
#浅拷贝
a = [1,2,3]
b = a  #指向同一个地址
print id(a)
print id(b)
#深拷贝
import copy
c = cpoy.deepcopy(a) #把地址中的内容复制一份，另存一个内存地址
print id(c)

