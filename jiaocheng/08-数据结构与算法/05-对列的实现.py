#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 May 2018 02:49:09 PM CST

# File Name: 05-对列的实现.py
# Description:

"""

class Queue(object):
    '''队列'''
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''往队列增加元素'''
        self.__list.append(item)

    def dequeue(self):
        '''从队列取元素'''
        return self.__list.pop(0)

    def is_empty(self):
        '''判断是否为空栈'''
        return self.__list == []

    def size(self):
        '''栈的元素个数'''
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
