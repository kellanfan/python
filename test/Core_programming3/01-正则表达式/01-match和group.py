#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Dec 2017 09:40:58 AM CST

# File Name: 01-match和group.py
# Description:

"""

import re
a = "abc-123"
reg = '(\w\w\w)-(\d\d\d)'
m = re.match(reg,a)
print m.group(1)
print m.group(2)
print m.groups()

#展示不同的子组排列
m = re.match('ab', 'ab')
print m.group()
print m.groups()

m = re.match('(ab)', 'ab')
print m.group()
print m.group(1)
print m.groups()

m = re.match('(a)(b)', 'ab')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()

m = re.match('(a(b))', 'ab')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()

