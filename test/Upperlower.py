#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Jun 2017 08:07:00 PM CST

# File Name: Upperlower.py
# Description:

"""
strlist = []
s = raw_input("input your name: ")
strlist.append(s)
def d(str):
    return str[0].upper() + str[1:].lower()
u = map(d, strlist)
print u
