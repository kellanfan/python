#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Sep 2017 06:29:23 PM CST

# File Name: 07-交换2个变量.py
# Description:

"""

a = 4
b = 5

#方式1
c = 0
c = a
a = b
b = c

#方式2
a = a + b
b = a - b
a = a - b

#方式3
a,b = b,a
