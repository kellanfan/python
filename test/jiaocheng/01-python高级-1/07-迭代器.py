#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 23 Jan 2018 07:42:05 PM CST

# File Name: 07-迭代器.py
# Description:

"""


#可迭代对象：
#一类是集合数据类型，如list, tuple, dict, set, str
#一类是generator,包括生成器和带yield的gneerator function

#判断是否可以迭代
from collections import Iterable

from collections import Iterator
print isinstance([],Iterable)
print isinstance(100,Iterable)

#可迭代不一定是迭代对象

print isinstance([],Iterator)
print isinstance((x for x in range(10)),Iterator)

#生成器都是迭代对象，但是list，dict，str虽然是Iterable，但不是Iterator
#可以用iter函数把list等变成Iterator

print isinstance(iter([]),Iterator)
print isinstance(iter('abc'),Iterator)
