#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 06 Feb 2018 08:35:25 PM CST

# File Name: 06-集合的用途.py
# Description:

"""

#集合去重
a=[1,2,2,3,4,5,3,4]
b = set(a)
a = list(b)
print(a)

#取交集或并集
c = "abcde"
d = set(c)
e = "dca"
f = set(e)
print(d&f) #取交集
print(d|f) #取并集
print(d-f) #差集
print(d^f) #
