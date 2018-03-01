#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 03:32:02 PM CST

# File Name: 03-多个fork.py
# Description:

"""

import os
ret = os.fork()
if ret == 0:
    print("---1---")
else:
    print("---2---")


ret = os.fork()
if ret == 0:
    print("---11---")
else:
    print("---22---")

