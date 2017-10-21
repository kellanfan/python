#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 19 Oct 2017 08:08:59 PM CST

# File Name: 10-文件备份应用-大文件.py
# Description: 通过文件备份的方式学习文件的读取和写入

"""
import sys
#要求：把文件复制成文件(副本)，如aa.txt备份成aa(副本).txt

#需要备份的文件
target_file = raw_input("请输入需要备份的文件名(需要后缀)：")

#尝试打开文件，已确认文件是否存在
try:
    f_read = open(target_file,'r')
except:
    print "没有这个文件！！！"
    sys.exit(1)

#格式化目标文件
#file_name = file.split('.')[0] + '(副本).' + file.split('.')[1] 这个情况只适合正常的文件名
position = file.rfind('.') #找到最右面的.，确认好位置，将“副本”放到中间
file_name = file[0:position] + '(副本)' + file[position:]

#以写入模式打开备份文件
f_write = open(file_name, 'w')

#循环读取文件内容后写到备份文件，这样防止文件过大导致内存溢出
while True:
    content = f_read.read(1024) #每次读取1024字节，可以调大一些
    if len(content) == 0: #当读取内容长度为0时，文件读完了
        break
    f_write.write(content)
    f_write.close()
f_read.close()
