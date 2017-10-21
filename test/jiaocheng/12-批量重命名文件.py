#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 21 Oct 2017 03:35:48 PM CST

# File Name: 12-批量重命名文件.py
# Description:

"""
import os
#获取文件夹名
dirname = raw_input("请输入文件夹名：")
#获取该文件夹中的文件名
file_names = os.listdir(dirname)
#跳转到对应文件夹
os.chdir(dirname)
#对获取的名字进行重命名
for file_name in file_names:
    os.rename(file_name, '[凯哥]-' + file_name)
