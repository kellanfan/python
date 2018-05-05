#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 27 Nov 2017 08:52:02 PM CST

# File Name: 23-__new__方法.py
# Description:

"""

class Dog(object):
    def __init__(self):
        print "init方法"

    def __del__(self):
        print "del方法"

    def __str__(self):
        print "stra方法"

    def __new__(cls): #cls此时是Dog指向的那个类对象，这样做相当于重写父类的__new__方法，此方法值负责创建对象，因为你重写了，最后要调用父类的new方法创建对象，否则就会出问题
        print "new方法"
        #print "id(cls)" 类的内存地址
        return object.__new__(cls) 
#print "id(Dog)" 内存地址一样，说明cls代表的就是指向的类对象
xtq = Dog() #这里做了3件事，
            #1.调用new方法创建对象，然后找了一个变量来接受new的返回值，这个返回值表示创建出来的对象的返回值
            #2.__init__(刚刚创建出来的对象的引用)
            #3.返回对象的引用
