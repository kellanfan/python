#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 06 Dec 2017 10:40:12 AM CST

# File Name: 30-给程序传参数.py
# Description: 使用sys.argv给函数传参数

"""

import sys

name = sys.argv[1]

print "欢迎 %s的到来！"%name
