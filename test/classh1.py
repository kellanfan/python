#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 01 Jul 2017 05:12:58 PM CST

# File Name: classh1.py
# Description:

"""

class Student(object):

    @property #python内置的装饰器负责把一个方法变成属性调用，把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):  #定义了一个getter方法
        return self._score

    @score.setter   #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
