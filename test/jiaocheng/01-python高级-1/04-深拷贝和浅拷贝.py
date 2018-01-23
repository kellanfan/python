#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 18 Jan 2018 07:52:29 PM CST

# File Name: 04-深拷贝和浅拷贝.py
# Description:

"""
#浅拷贝
a = [1,2,3]
b = a  #指向同一个地址
print id(a)
print id(b)
#深拷贝
import copy
c = cpoy.deepcopy(a) #把地址中的内容复制一份，另存一个内存地址
print id(c)

#更深层次的深拷贝
a = [1,2,3]
b = [4,5,6]
c = [a,b]
d = c #浅拷贝
e = copy.deepcopy(c) #深拷贝，会把指向的内容也拷贝
a.append(4)
id(c)
id(e)


a = [1,2,3]
b = [4,5,6]
c = [a,b]
e = copy.copy(c) #拷贝，只把引用拷贝了
a.append(4)
id(c)
id(e)

#使用copy时，他会根据拷贝的数据类型是可变类型还是不可变类型有不同的处理方式
a = [1,2,3]
b = [4,5,6]
c = [a,b]
e = copy.copy(c)
id(c)
id(e)

