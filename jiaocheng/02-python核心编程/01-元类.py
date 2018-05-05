#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 29 Jan 2018 07:22:10 PM CST

# File Name: 01-元类.py
# Description:

"""

#首先，在python中一切皆对象。元类就是创建类
#创建元类的方法


def printnum(self):
    print("----num---%d---"%self.num)

Test = type('Test', (), {"printnum":printnum}) #type(类名，(父类)，{属性})
t1 = Test()
print(t1.__class__) #查看是哪个类创建的
print(Test.__class__)
