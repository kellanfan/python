#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Mon 11 Sep 2017 06:19:31 PM CST

# File Name: budingchangcanshu.py
# Description:不定长参数，*args 参数前面加个*，就是多余形参的值放到这里组成一个元组，用于不确定参数数量时使用

"""


def sum_nums(a,b,*args):
    num1 = a + b
    for num in args:
        num1 += num
    return num1

def print_num(a,b,c=33,*args,**kwargs): #默认参数，不定长函数的2种，元组和字典形式
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

print_num(1,2,3,4,5,6,task=22,job=333)
print_num(1,2,3,task=22,job=333)
print_num(1,2,task=22,job=333)
print_num(1,2,3,4,5)
print_num(1,2)
print(sum_nums(1,2,3,4,5,6))
print(sum_nums(1,2,3))
