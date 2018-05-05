#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 20 Apr 2018 03:52:37 PM CST

# File Name: 10-getattr.py
# Description:

"""


class Foo(object):
    def __init__(self):
        pass
    
    #当对未定义的属性名称和实例进行点号运算时，就会用属性名作为字符串调用这个方法。
    def __getattr__(self, item):
        print(item,)
        return self
    
    #把类的对象转成字符串
    def __str__(self):
        return ""


print(Foo().aa.bb.cc)
