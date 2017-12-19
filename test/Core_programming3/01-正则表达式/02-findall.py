#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Dec 2017 10:16:13 AM CST

# File Name: 02-findall.py
# Description:

"""
import re
s = 'This and that'

print re.findall('(th\w+) and (th\w+)',s, re.I)
print re.finditer('(th\w+) and (th\w+)',s,re.I).next().groups()
print re.finditer('(th\w+) and (th\w+)',s,re.I).next().group(1)
print re.finditer('(th\w+) and (th\w+)',s,re.I).next().group(2)
print [g.groups() for g in re.finditer('(th\w+) and (th\w+)',s,re.I)]
