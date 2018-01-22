#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 05 Nov 2017 04:15:08 PM CST

# File Name: 22-实例方法类方法和静态方法.py
# Description:

"""

class Game(object):
    #类属性
    num = 0
    #实例方法
    def __init__(self, new_name):
        self.name = new_name
    #类方法
    @classmethod
    def add_num(cls): #cls类似于self，指向类
        cls.num = 100
    #静态方法
    @staticmethod   #与实例和类关系不大的可以使用静态方法
    def print_version():
        print "-------------"
        print " version:2.1"
        print "-------------"

game = Game()
#Game.add_num() 可以通过类调用类方法，也可以通过类创建出来的对象去调用
game.add_num() 
print Game.num

Game.print_version()
#game.print_version()  同类方法

