#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 25 Jan 2018 07:36:56 PM CST

# File Name: 15-通用装饰器.py
# Description:

"""
def func(function):
    def func_in(*args, **kwargs):
        x = function(*args, **kwargs)
        return x

    return func_in


#如果不需要返回值，那么返回值就是none而
