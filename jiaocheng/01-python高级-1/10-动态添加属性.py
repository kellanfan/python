#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 26 Jan 2018 01:55:42 PM CST

# File Name: 10-动态添加属性.py
# Description:

"""

class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

a = Person('fankai',100)
print(a.name)
a.addr = 'pek' #动态添加对象属性
print(a.addr)

Person.num = 100 #动态添加类属性
print(a.num)
