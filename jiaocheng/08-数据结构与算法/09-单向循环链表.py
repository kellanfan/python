#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 06 May 2018 09:29:53 AM CST

# File Name: 09-单向循环链表.py
# Description:

"""
from Linklist import LinkList

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleCircliLinkList(LinkList):
    '''单向循环链表'''
    def __init__(self, node=None):
        self.head = node
        if node:
            node.next = node

    def lenth(self):
        '''获取链表长度'''
        if is_empty():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travl(self):
        '''遍历链表'''
        if self.head == None:
            return None
        cur = self.head
        while cur.next != self.head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item)

    def append(self, item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            cur.next = node

    def add(self, item):
        '''链表头部添加 '''
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head
            self.head = node

    def insert(self, pos, item):
        '''在链表的指定位置添加，这里以0为开始'''
        if pos < 0:
           self.add(item)
        elif pos > self.lenth() - 1:
           self.append(item)
        else:
            pre = self.head
            count = 0
            #循环找到要插入位置之前的一个
            while count < pos - 1:
                pre = pre.next
                count += 1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def search(self, item):
        '''从链表中查询'''
        if self.is_empty():
            return False
        cur = self.head
        while cur.next != self.head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        #退出循环cur指向尾节点，判断尾节点是否与值相等
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        '''从链表中删除元素'''
        cur = self.head
        pre = None
        while cur.next != self.head:
            if cur.item == item:
                #判断是否是头结点
                if self.head == cur:
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = cur.next
                    rear.next = self.head
                else:
                    #中间节点
                    pre.next = cur.next
                retrun
            else:
                #跳到下一个节点，先移动pre才能移动cur
                pre = cur
                cur = cur.next
        #尾节点
        if cur.item == item:
            if cur == self.head #只有一个节点
                self.head = None
            else:
                pre.next = cur.next
