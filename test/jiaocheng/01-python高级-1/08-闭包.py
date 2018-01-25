#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 23 Jan 2018 08:15:19 PM CST

# File Name: 08-闭包.py
# Description:

"""
#闭包：在一个函数内定义一个函数,内部的函数接收外部函数的参数，外部函数返回内部函数的引用。
#
def test(num):
    print('---1---')

    def test_in(num1):
        print('---2----')
        print(num + num1)

    return test_in

ret = test(100)
ret(200)
