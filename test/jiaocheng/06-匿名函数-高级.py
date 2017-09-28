#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Sep 2017 06:14:54 PM CST

# File Name: 06-匿名函数-高级.py
# Description:

"""

def test(a,b,func):
    result = func(a,b)
    print(result)
func_new = input("请输入一个匿名函数：")
#如果是python3，这么直接输入会报错，需要使用eval函数将输入的字符串还原成原来的样子才行
func_new = eval(func_new)
test(11,22,func_new)
