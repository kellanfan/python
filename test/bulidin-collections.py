#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 25 Jul 2017 10:12:43 AM CST

# File Name: bulidin-collections.py
# Description: namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便.

"""

from collections import namedtuple
Point = namedtuple('Point',['x', 'y'])
p = Point(1, 2)
print p
print p.x
print p.y
