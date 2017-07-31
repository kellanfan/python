#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 31 Jul 2017 02:25:46 PM CST

# File Name: memcache-test.py
# Description:

"""


import memcache
mc = memcache.Client(['127.0.0.1:11211'],debug=0)
mc.set("foo","bar")
vlue = mc.get("foo")
print vlue
