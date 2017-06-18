#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 18 Jun 2017 09:41:22 AM CST

# File Name: attr.py
# Description:

"""

class Myclass(object):
    def __init__(self):
        self.x = 10
    def power(self):
        return self.x * self.x

f = Myclass()
print "有属性x吗？ %s" % hasattr(f, 'x')
print "有属性y吗？ %s" % hasattr(f, 'y')
print "设置属性y"
setattr(f, 'y', 100)
print "设置完成，属性y值是？%s" % getattr(f, 'y')
print "如果没有属性z，获取失败，则返回404"
print getattr(f, 'z', 404)
