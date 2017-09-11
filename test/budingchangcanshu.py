#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Mon 11 Sep 2017 06:19:31 PM CST

# File Name: budingchangcanshu.py
# Description:不定长参数，*args 参数前面加个*，就是多余形参的值放到这里组成一个元组，用于不确定参数数量时使用

"""


def sum_nums(a,b,*args):
    num1 = 0
    for num in args:
        num1 += num
    return a + b + num1

def print_num(a,b,*args):
    print a
    print b
    print args

print_num(1,2,3,4,5,6)
print_num(1,2,3)
print sum_nums(1,2,3,4,5,6)
print sum_nums(1,2,3)
