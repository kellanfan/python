#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 23 Jan 2018 07:02:02 PM CST

# File Name: 05-property.py
# Description:

"""
class Test(object):
    def __init__(self):
        self.__num = 100
    
    @property
    def num(self):   #注意到这个函数名和下面的函数名一样，这个表示的是一个get方法
        return self.__num
    
    @num.setter      #下面的函数表示的是set方法，
    def num(self, new_num):
        self.__num = new_num

t = Test()
t.num = 9 #相当于调用了 t.setnum(9)
print t.num #相当于调用了 t.getnum()

#注意点:
#t.num到底调用哪个，要根据实际场景来判断
#1.如果是给t.num赋值，那么一定调用setnum()
#2.如果是获取t.num的值，那么一定调用getnum()
#property的作用：相当于把方法进行了封装，开发者在对属性设置数据的时候方便
