#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 30 Oct 2017 06:35:09 PM CST

# File Name: 14-隐藏属性.py
# Description:

"""
#定义一个类，属性的定义尽量使用方法去定义
class Dog:
    def set_age(self,new_age):
        if new_age>0 and new_age<=100: #可以加判断对属性的定义进行限制
            self.age = new_age
        else:
            self.age = 0
    
    def get_age(self):
        return self.age
#定义一个对象
dog = Dog()
dog.set_age(-10)
print dog.get_age()

