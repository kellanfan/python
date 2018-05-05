#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 29 Jan 2018 08:50:38 PM CST

# File Name: 03-垃圾回收机制.py
# Description:

"""
#目的是理解python的垃圾回收机制是怎么做的：
#1.小整数对象池(-5,257),这是python解释器启动时就创建好的，常驻内存
#单个字符共用对象，常驻内存
#单个单词不可修改，默认开启intern机制，共用对象，引用计数为0则销毁
a = 100
b = 100
print(id(a))
print(id(b))
#2.引用计数，一旦引用没有，内存就直接释放了


#总结，GC 垃圾回收策略
#python以引用计数为主，标记-清除和隔代收集2种机制为辅的策略
 
