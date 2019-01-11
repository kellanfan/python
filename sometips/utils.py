#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 10 Jan 2019 12:00:36 PM CST

# File Name: utils.py
# Description: 这里会记录一些小技巧函数

"""

def utf8str(s):
    #返回utf8编码的字符串
    encoding = 'utf-8'
    if not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            return unicode(s).encode(encoding)
    elif isinstance(s, unicode):
        return s.encode(encoding)
    else:
        return s

def encode_pairs(pairs, lsep, tsep):
    """Return string joined by seperator
    >>> p = [('a',1), ('b',2)]
    >>> encode_pairs(p, '|', ':')
    'a:1|b:2'
    """
    return lsep.join([tsep.join([utf8str(i) for i in p]) for p in pairs])


