#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 27 Jan 2018 09:34:48 PM CST

# File Name: 01-类装饰器.py
# Description:

"""

class Test(object):
    def __init__(self,func):
        print("开始初始化")
        print("引用的方法是%s"%func.__name__)
        self.__func = func #__func指向下面的函数

    def __call__(self):
        print("调用装饰器中的方法")
        self.__func()


@Test #相当于test=Test(test)
def test():
    print("----test----")

test()
