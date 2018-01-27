#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 08:36:20 PM CST

# File Name: 01-LEGB.py
# Description:

"""
#LEGB规则
#查找一个符号对应的对象
#locals --> enclosing function --> globals --> buildin
#locals当前所在的命名空间
#enclosing 外部嵌套函数的命名空间（闭包中常见）
#globals 全局变量
#buildin 内建，系统自带的

a = 100
def test():
    a = 200
    def test1():
        a = 300
        print("num=%d"%a)
    return test1

ret = test()
ret()
