#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Wed 16 Aug 2017 09:34:17 AM CST

# File Name: bulidin-diedai.py
# Description:

"""

import itertools
a = itertools.count(1)
#count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
for i in a:
    print(i)
#cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABCDEF')
for c in cs:
    print(c)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 10)
for n in ns:
    print(n)

#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
        print c
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group) # 为什么这里要用list()函数呢？

#忽略大小写
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)


#map函数，接收2个参数，一个函数，一个list，map将传入的函数依次作用到list的每个元素，并把结果作为新的list返回
for i in map(lambda x:x*x, [1,2,3,4,5,6,7,8]):
    print(i)

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
import functools import reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5,6,7,8,9,10]))

#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
