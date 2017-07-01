#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 01 Jul 2017 06:16:29 PM CST

# File Name: ex_chain.py
# Description: 现在很多网站都搞REST API，像：http://api.server/user/timeline/list  如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改，利用完全动态的__getattr__，我们可以写出一个链式调用

"""

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list
