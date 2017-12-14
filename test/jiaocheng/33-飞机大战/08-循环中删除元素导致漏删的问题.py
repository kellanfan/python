#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 13 Dec 2017 11:24:19 AM CST

# File Name: 08-循环中删除元素导致漏删的问题.py
# Description:

"""

a = [11,22,33,44,55,66,77]
for i in a:
    if i == 33 or i == 44:
        a.remove(i)

print a #会漏删44，这是由于当删除33后，44及以后的元素会前移，导致下一个元素变成55了。
#子弹越界没有这个问题是，一直在调用display，漏的元素会在下次调用时删除
#解决方法，新建一个list存储要删除的元素，最好统一删除
'''
a = [11,22,33,44,55,66,77]
b = []

for i in a:
    if i == 33 or i == 44:
        b.append(i)
for i in b:
    a.remove(i)

'''
