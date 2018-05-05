#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 May 2018 02:13:51 PM CST

# File Name: 04-栈的实现.py
# Description: 通过list实现栈，也可以使用链表

"""
class Stack(object):
    '''栈'''
    def __init__(self):
        self.__list = []

    def push(self, item):
        '''增加元素'''
        self.__list.append(item)

    def pop(self):
        '''弹出栈顶元素'''
        return self.__list.pop()

    def peek(self):
        '''返回栈顶元素'''
        if self.__list:
           return self.__list[-1]
        else:
           return None

    def is_empty(self):
        '''判断是否为空栈'''
        return self.__list == []

    def size(self):
        '''栈的元素个数'''
        return len(self.__list)
           

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size())
