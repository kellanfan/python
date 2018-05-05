#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 26 Apr 2018 10:58:33 AM CST

# File Name: 01-test.py
# Description: a+b+c=1000 并且 a^2 + b^2 = c^2 的可能性

"""

#最简单的枚举法
import time
start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d"%(a, b, c))
end_time = time.time()
print("use time: %d"%(end_time - start_time))
print("Done...")
