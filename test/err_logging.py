#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 08 Jul 2017 09:21:17 AM CST

# File Name: err_logging.py
# Description:

"""

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
