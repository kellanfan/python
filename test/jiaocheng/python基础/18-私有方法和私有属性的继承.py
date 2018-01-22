#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 02 Nov 2017 08:41:59 PM CST

# File Name: 18-私有方法和私有属性的继承.py
# Description:

"""
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def test1(self):
        print "test1"
    def __test2(self):
        print "test2"
    def test3(self):
        self.__test2()
        print self.__num2
class B(A):
    def test4(self):
        self.__test2()
        print self.__num2

b = B()
b.test1()
#b.__test2() #私有方法无法继承
print b.num1
#print b.__num1 #私有属性无法继承
b.test3
b.test4 #父类自己调用自己的私有方法或属性可以，但是子类不知直接调用

#如果调用的是 继承的父类中的共有方法,可以在这个共有方法中访问父类的私有方法和私有属性
#但是在子类的共有方法中不能调用继承的父类中的私有方法和私有属性

