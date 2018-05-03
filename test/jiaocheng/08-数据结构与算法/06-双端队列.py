#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 May 2018 04:46:37 PM CST

# File Name: 06-双端队列.py
# Description:

"""

class Dqueue(object):
    '''双端队列'''
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        '''从队头加入元素'''
        self.__list.insert(0, item)

    def add_rear(self, item):
        '''从队尾加入元素'''
        self.__lsit.append(item)

    def remove_front(self):
        '''从对头删除元素'''
        return self.__list.pop(0)

    def remove_rear(self):
        '''从队尾删除元素'''
        return self.__list.pop()

    def is_empty(self):
        '''判断队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回队列元素个数'''
        return len(self.__list)


if __name__ == '__main__':
    pass
