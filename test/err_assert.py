#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 08 Jul 2017 11:41:15 AM CST

# File Name: err_assert.py
# Description:

"""

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo(0)
