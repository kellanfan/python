#!/usr/bin/python
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'kellan fan'

import sys


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 4:
        return _private_1(name)
    else:
        return _private_2(name)


def test():
    args = sys.argv
    if len(args)==1:
        print "hello world"
    elif len(args)==2:
        print "hello,%s" %args[1]
    else:
        print greeting(args[1:])

if __name__ == '__main__':
    test()
