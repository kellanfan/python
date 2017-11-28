#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Nov 2017 06:48:09 PM CST

# File Name: 24-创建单例.py
# Description: 单例的意思就是只创建一个对象，所有引用都指向这个对象

"""

class Dog(object):
    __instance = None  #定义一个类属性
    def __new__(cls): #重写new方法
        if cls.__instance == None: #如果类属性为空，那么就使用父类的new方法创建一个对象，并使用这个类属性指向这个对象，并保存到这个类属性中
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else: 
            return cls.__instance  #直接返回上次创建的对象的引用

a = Dog()
print id(a)
b = Dog() #第二次创建的时候，类属性不为空，所以直接返回上次创建的对象的引用
print id(b)
