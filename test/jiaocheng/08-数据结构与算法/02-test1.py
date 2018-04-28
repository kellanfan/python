#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 26 Apr 2018 11:35:39 AM CST

# File Name: 02-test1.py
# Description: a+b+c=1000 并且 a^2 + b^2 = c^2 的可能性

"""

import time

import time
start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d"%(a, b, c))
end_time = time.time()
print("use time: %d"%(end_time - start_time))
print("Done...")
