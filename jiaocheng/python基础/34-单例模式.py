#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 10 Mar 2019 07:48:20 PM CST

# File Name: 34-单例模式.py
# Description:  确保某一类只有一个实例，而且自行实例化并向整个系统提供这个实例，
        称为单例类
"""

class Singlecls(object):
    __instance = None
    __first_init = False
    def __new__(cls,name,age):
        #如果是第一次创建，那么就调用父类的__new__创建实例，如果不是，那么就把上次创建的类return，这样就能保证所有创建的实例都指向同一个实例，下面的__init__也是一样的道理
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,name,age):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singlecls.__first_init = True


a = Singlecls('kellan',14)
b = Singlecls('aaa',34)

print(id(a))
print(id(b))

print(a.age)
print(b.age)

a.age = 20

print(b.age)
