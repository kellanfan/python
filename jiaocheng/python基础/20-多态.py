#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 05 Nov 2017 03:05:50 PM CST

# File Name: 20-多态.py
# Description: 面向对象的3大要素，封装、继承、多态
        所谓多态，就是定义时的类型和运行时的类型不一样

"""

class Dog(object):
    def print_self(self):
        print "大家好"
class Xiaotq(Dog):
    def print_self(self):
        print "hello"

def introduce(temp):
    temp.print_self()
dog1 = Dog()
dog2 = Xiaotq()
introduce(dog1)
introduce(dog2)
