#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 12 Jun 2017 06:57:38 PM CST

# File Name: partialtest.py
# Description:

"""

import functools
int2 = functools.partial(int, base=2)
print int2('1000100')
