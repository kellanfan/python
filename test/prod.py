#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Jun 2017 08:35:49 PM CST

# File Name: prod.py
# Description:

"""
def prod(l):
    def j(x, y):
        return x * y
    def char2num(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(j, map(char2num, l))


L = '12345667'
a = prod(L)
print a
