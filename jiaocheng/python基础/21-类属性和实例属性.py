#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 05 Nov 2017 03:46:44 PM CST

# File Name: 21-类属性和实例属性.py
# Description: 在实例或对象中没有存储方法，而是有一个特殊的属性指向类的方法
    实力属性：和具体的某个实例对象有关，并且一个实例对象与另一个实例对象是不共享属性的
    类属性：类属性属于类对象，多个实例对象之间共享同一个类属性
    如果需要在类外修改 类属性 ，必须通过 类对象 去引用，然后进行修改。
    如果通过实例对象去引用，会产生一个同名的 实例属性 ，这种方式修改
    的是 实例属性 ，不会影响到 类属性 ，并且之后如果通过实例对象去引
    用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是 实例属
    性 ，除非删除了该 实例属性 。
"""   

class Tool(object):
    #类属性
    num = 0 #类似于一个全局变量
    def __init__(self, new_name):
        #实例属性
        self.name = new_name
        Tool.num += 1 #使用的时候要注意，要实用类名去标记
tool1 = Tool("shuitong")
tool2 = Tool("tiechan")
tool3 = Tool("haha")
print Tool.num
