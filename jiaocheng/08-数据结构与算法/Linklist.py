#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 05 May 2018 08:17:40 PM CST

# File Name: Linklist.py
# Description:

"""

class LinkList(object):
    '''链表'''
    def __init__(self, node=None):
        self.head = node #由于需要被子类继承，所以不能是私有属性，不能是__head

    def is_empty(self):
        '''判断是否为空链表'''
        return self.head == None

    def lenth(self):
        '''获取链表长度'''
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travl(self):
        '''遍历链表'''
        cur = self.head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print('')

    def search(self, item):
        '''从链表中查询'''
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

