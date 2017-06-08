#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 08 Jun 2017 08:09:58 PM CST

# File Name: decorator.py
# Description:

"""

import functools

def log(begin_text,end_text):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s()' %(begin_text, func.__name__)
            return func(*args,**kw)
        def wrapper1(*args,**kw):
            print '%s %s()' %(end_text, func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorate

@log('begin','end')
def now():
    print '2017-06-08'

now()
