#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 20 Sep 2017 03:28:57 PM CST

# File Name: sort_errorlog.py
# Description:

"""

import os, sys, re

def filename(filepath, filetype):
    filename = []  
    for root,dirs,files in os.walk(filepath):  
        for i in files:  
            if filetype in i:  
                filename.append(i)  
    return filename  
def re_group(conent):
    reg = r''
os.chdir('/notifier')
for file1 in filename('/notifier', 'alert'):
    with open(file1,'r') as f:
        content = f.read()

