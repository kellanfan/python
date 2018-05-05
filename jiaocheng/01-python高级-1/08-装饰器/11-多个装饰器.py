#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 02:55:08 PM CST

# File Name: 11-多个装饰器.py
# Description:

"""

def makeBlod(func):
    def wrapped():
        return "<b>" + func() + "</b>"
    return wrapped

def makeItalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped

@makeBlod
@makeItalic
def test3():
    return "hello world"

ret = test3()
print(ret)
