#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 19 Oct 2017 08:08:59 PM CST

# File Name: 09-文件备份应用.py
# Description: 通过文件备份的方式学习文件的读取和写入

"""
import sys
#要求：把文件复制成文件(副本)，如aa.txt备份成aa(副本).txt

#需要备份的文件
tar_file = raw_input("请输入需要备份的文件名(需要后缀)：")

#尝试打开文件，已确认文件是否存在
def read_file(file):
    try:
        f = open(file,'r')
    except:
        print "没有这个文件！！！"
        sys.exit(1)
    #读取文件内容
    content = f.read()
    f.close()
    return content
#将内容写入副本文件
def write_file(file, content):
#    file_name = file.split('.')[0] + '(副本).' + file.split('.')[1] 这个情况只适合正常的文件名
    position = file.rfind('.')
    file_name = file[0:position] + '(副本)' + file[position:]
    f = open(file_name, 'w')
    
    f.write(content)
    f.close()

if __name__ == '__main__':
    content = read_file(tar_file)
    write_file(tar_file, content)
    print "Done..."
