#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 Aug 2017 06:58:04 PM CST

# File Name: checkbmp.py
# Description: '>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。

"""

import struct

def checkbmp(file):
    try:
        with open(file, 'r') as f:
            string = f.read(30)
        t = struct.unpack('<ccIIIIIIHH', string)
        if t[0] == 'B' and t[1] == 'M':
            print("%s is bmp file...and Size(%s * %s); Colornumber(%s)" % (file, t[6], t[7], t[9]))
        else:
            print("%s is not bmp file...")
    except IOError:
        print("please input right filename...")

checkbmp('aa.bmp')
checkbmp('bao.py')
