#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Nov 2017 08:15:49 PM CST

# File Name: 27-抛出自定义异常.py
# Description:

"""

class ShotInputException(Exception): #其实所有异常项目都是一个类，而Exception是所有异常的父类
    '''自定义异常类'''
    def __init__(self, lenth, atlease):
        self.lenth = lenth
        self.atlease = atlease

def main():
    try:
        s = raw_input("请输入--> ")
        if len(s) < 3:
            #raise引发一个自定义的异常
            raise ShotInputException(len(s), 3)
    except ShotInputException as result: #result就是个变量指向自定义异常类所创建的对象
        print "ShotInputException: 输入长度是：%d, 长度至少应为: %d" %(result.lenth, result.atlease)

    else:
        print "没有异常"

main()
