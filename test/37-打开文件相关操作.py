# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   37-打开文件相关操作.py
@Time    :   2019/05/14 13:56:59
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

#f = open("file.txt","w")
f = open("file.txt","r")
print("文件名：", f.name)
print("文件是否关闭：", f.closed)
print("访问模式：", f.mode)
print("末尾是否强制加空格 : ", f.softspace)
#f.write( "www.runoob.com!\nVery good site!\n")
st = f.read(10)
print(st)

# 查找当前位置
position = f.tell();
print("当前文件位置 : ", position)
 
# 把指针再次重新定位到文件开头
position = f.seek(0, 0);
str = f.read(10);
print("重新读取字符串 : ", str)

position = f.seek(12, 0);
str = f.read(10);
print("将指针定位到12，重新读取字符串 : ", str)
f.close()
