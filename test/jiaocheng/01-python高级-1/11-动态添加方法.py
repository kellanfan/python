#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 26 Jan 2018 01:59:56 PM CST

# File Name: 11-动态添加方法.py
# Description:

"""
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("%s正在吃饭..."%self.name)

def run(self):
    print("%s正在跑..."%self.name)

a = Person('ken',11)
#a.run = run #虽然a的对象中run属性已经指向了第19行的函数，但是还不正确
#a.run()     #因为run属性指向的函数是后添加的,即a.run()的时候并没有把a当做
            #第一个参数，导致第19行调用的时候，出现缺少参数的问题

import types
a.run = types.MethodType(run, a)
a.run()
   

@staticmethod
def printnum():
    print("100")
a.printnum = printnum
a.printnum()

@classmethod
def printaa(cls):
    print("aaaaa")

a.printaa = printaa
a.printaa()
