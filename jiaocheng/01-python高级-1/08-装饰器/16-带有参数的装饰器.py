#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 07:56:28 PM CST

# File Name: 16-带有参数的装饰器.py
# Description:

"""

def func_arg(arg):
    def func(function):
        def func_in():
            print("arg=%s" %arg)
            if arg == 'hehe':
                function()
                function()
            else:
                function()
            
        return func_in
    return func
#1. 先执行func_arg("hehe")这个函数之歌函数return的结果是func这个函数
#2. 执行完后就变成了@func
#3. 使用@func对test进行装饰
@func_arg("hehe")
def test():
    print("test")
#带有参数的装饰器，能够起到在运行时，有不同功能
test()
