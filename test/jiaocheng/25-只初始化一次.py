#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Nov 2017 06:48:09 PM CST

# File Name: 24-创建单例.py
# Description: 只初始化的意思是，只把对象属性初始化一次

"""

class Dog(object):
    __instance = None  #定义一个类属性
    __init_flag = False  #定义类属性做为是否初始化的标记
    def __new__(cls,name): #重写new方法   #这个name参数只是为了不报错，new方法不用
        if cls.__instance == None: #如果类属性为空，那么就使用父类的new方法创建一个对象，并使用这个类属性指向这个对象，并保存到这个类属性中
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else: 
            return cls.__instance  #直接返回上次创建的对象的引用

    def __init__(self, name):
#        self.name = name  单纯这么写的话，name属性会变
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True

a = Dog("小黑")
print id(a)
print a.name
b = Dog("小白") #第二次创建的时候，类属性不为空，所以直接返回上次创建的对象的引用
print id(b)
print b.name
