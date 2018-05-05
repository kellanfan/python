#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 23 Jan 2018 08:55:11 PM CST

# File Name: 09-闭包应用.py
# Description:

"""

def conf(a,b):
    def line(x):
        return a*x+b

    return line

line1 = conf(1,2)
print(line1(1))

line2 = conf(2,3)
print(line2(1))


#不用闭包的方式的话
#def line(a,b,x)
#    return a*x+b
#
#line(1,2,3)

#这样的方式要传的参数较多，而且如果a,b参数不想变的话，也要穿，不好复用
