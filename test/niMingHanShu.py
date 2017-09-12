#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Tue 12 Sep 2017 05:56:57 PM CST

# File Name: niMingHanShu.py
# Description: 匿名函数 格式  变量 =  lambda 参数：式子   就是变量指向一个匿名函数
调用：变量(参数)
匿名函数 ：的后面式子自带return，所以一般可以理解为
变量 =  lambda 参数：return 式子
因为是这样，所以简单的函数可以用匿名函数，但是复杂的函数还是要使用def定义
"""


def suma(a,b):
    a + b
#没有return就没办法输出返回值
suma(11,22)


#定义匿名函数
func = lambda a,b:a+b
#自带retuen
print func(11,22)
