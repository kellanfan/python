#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 18 Jan 2018 06:53:02 PM CST

# File Name: 02-重新导入模块.py
# Description: reload函数在imp模块中，它的作用是，当你的模块有修改，有不想退出程序再进的时候可以使用这个函数重新导入模块

"""

from imp import *

import test

test.test()
