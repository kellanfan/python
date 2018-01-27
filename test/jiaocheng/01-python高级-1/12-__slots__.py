#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 26 Jan 2018 08:27:00 PM CST

# File Name: 12-__slots__.py
# Description:

"""

class Person(object):
    __slots__ = ("name", "age") #__slots__的作用是保护属性的多少，不可以随意添加
                                #仅对当前类实例起作用，对继承的子类是不起作用的

    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

p = Person("aa",12)
p.addr = "aaa"
