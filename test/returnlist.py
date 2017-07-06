#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 05 Jul 2017 07:01:20 PM CST

# File Name: returnlist.py
# Description:

"""

def add_element(a, b, c):
    d = a + b
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    return list

l = add_element(1, 23, 5)
print l
