#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 04 Nov 2017 02:34:15 PM CST

# File Name: 19-多继承.py
# Description:

"""
"""
class Base(object):
    def test(self):
        print "----base"

class A(Base):
    def test1(self):
        print "----test1"
    
class B(Base):
    def test2(self):
        print "----test2"

class C(A,B): 多继承，继承了多个类的方法
    pass

c = C()
c.test1()
"""

class Base(object):
    def test(self):
        print "----base"

class A(Base):
    def test(self):
        print "----A"
    
class B(Base):
    def test(self):
        print "----B"

class C(A,B):
    pass

c = C()
c.test()
print C.__mro__  #类名.__mro__显示搜素方法的顺序，使用C3算法决定着调用一个方法的时候搜索的顺序，如果在某个
                 #类中找到了方法，那么就停止搜素。所以尽量不要再类里面出现相同的方法。
