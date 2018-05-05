#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 11:45:33 AM CST

# File Name: 02-fork全局变量.py
# Description:

"""

import os
import time
#全局变量在多个进程中不共享
g_num = 100

ret = os.fork()
if ret==0:
    print("----1----")
    g_num += 1
    print("---1---g_num=%d"%g_num)
else:
    time.sleep(3)
    print("----2----")
    print("---2---g_num=%d"%g_num)
    
