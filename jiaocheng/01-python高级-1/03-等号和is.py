#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 18 Jan 2018 07:34:44 PM CST

# File Name: 03-等号和is.py
# Description:

"""
a = [1,2,3]
b = [1,2,3]
print(a == b) #比较两个对象是否相等
print(a is b) #比较两个引用是否指向同一个对象

c = 100
d = 100
print(a is b) #-5到126是相同的，但是超过这个范围就不同了
