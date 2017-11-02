#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 02 Nov 2017 07:54:00 PM CST

# File Name: 16-继承.py
# Description: 继承是子类可以使用父类的方法，可以多层继承

"""

class Animal: #父类，基类
    def eat(self):
        print "---吃---"
    def dirik(self):
        print "---喝---"
class Cat(Animal): #括号里写的就是父类，继承父类的方法 子类，派生类
    def catch(self):
        print "---抓老鼠---"

aa = Animal()
aa.eat()
tom = Cat()
tom.eat()
tom.catch()
