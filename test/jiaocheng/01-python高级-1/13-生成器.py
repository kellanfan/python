#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 27 Jan 2018 10:51:42 AM CST

# File Name: 13-生成器.py
# Description:

"""

#第一种方法，就是把列表生成式的[]改成()

a = (x*2 for x in range(10000))
print(next(a))

#第二种方法，就是写函数，用yield
