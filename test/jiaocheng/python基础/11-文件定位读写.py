#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 21 Oct 2017 03:12:00 PM CST

# File Name: 11-文件定位读写.py
# Description:
当不想从开头读写时可以使用seek函数
seek(offset, form)
    offset 偏移量 正数向右移动，负数向左移动（Python3不支持负数）
    form    0 文件开头
            1 当前位置
            2 文件末尾
tell() 可以告诉你当前位置
"""
#读取一个文件
f = open('10-文件备份应用-大文件.py')
#先读取文件到文件的第3个位置，也就是读3个数
print f.read(3)
print "当前位置为 %d" % f.tell()
#向右偏移5个字符，读取
f.seek(5,1)
print f.read(1)

f.close()

#写也是类似，只不是要注意打开方式是读写方式打开，其次当你写完一段后，你的当前位置是写的内容的末尾位置，所以想要读取刚才写入的内容你要先向前偏移，或者跳到文件开头再读才行
