#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 01 Jul 2017 04:37:24 PM CST

# File Name: ex_slots.py
# Description: 由于'aa'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__

"""

class Student(object):
    __slots__ = ('name', 'age')

s = Student()

s.name = 'kellan'
s.age = 23
s.aa = 'ss' 

class Hstudent(Student):
    pass


g = Hstudent()
g.aa = 99
