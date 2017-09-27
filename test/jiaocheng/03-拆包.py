#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Mon 11 Sep 2017 06:46:24 PM CST

# File Name: chaibao.py
# Description: 对参数进行拆包

"""

def print_canshu(a,b,c=33,*args,**kwargs):
    print a
    print b
    print c
    print args
    print kwargs
    print '='*30

A = (44,55,66)
B = {'name':'kellan', 'age':24}
print_canshu(11,22,33,A,B) #当给函数传参时,不加*，就算是元组或字典，都默认是一个单一的参数，加*后，就是让函数知道
print_canshu(11,22,33,*A,**B) #这个参数是一个元组或者字典的形式，让函数进行拆包，并放入对应的位置。

#在Python中任何的赋值其实都是引用，变量名指向的不是内存中的值，而是这个值的内存地址，所以a = 100, a = b ，这里a，b都是指向内存中100这个值的内存地址

aa = 100
bb = aa
print id(aa)
print id(bb)
#这里说一下，可变类型和不可变类型:不可变类型有：数字，字符，元组，可变类型有：列表，字典
C = {'name':'aa',111:'1231',(11,22):'ascdsa'}
print C #只有不可变类型才能作为key，因为字典在内存中的保存是这样的，对key进行hash，得出来的值就是value中的内存位置。所以不能用可变类型来做key。

