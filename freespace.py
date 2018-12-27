#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 09 Sep 2018 09:20:09 PM CST

# File Name: freespace.py
# Description:

"""

import os
dirlist = ['/var/log', '/tmp']
for dir in dirlist:
    filelist = os.listdir(dir)
    for i in range(0,len(filelist)):
        path = os.path.join(dir,filelist[i])
        if os.path.isfile(path):
            if os.path.getsize(path) >= 10240000 and path.endswith('.log'):
                os.remove(path)
                print("clean ok...")
