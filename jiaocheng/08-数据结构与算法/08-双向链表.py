#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 05 May 2018 08:06:25 PM CST

# File Name: 08-双向链表.py
# Description:

"""
from Linklist import LinkList

class Node(object):
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class DoubleLinkList(LinkList):
    '''双链表'''
    def append(self, item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty(): #如果是空链表，直接将head指向node即可
            print(self.head)
            self.head = node
        else:
            cur = self.head #游标指向第一个元素
            while cur.next != None:
                cur = cur.next #游标指向下一个元素，只到最后一个元素
            cur.next = node
            node.prev = cur

    def add(self, item):
        '''链表头部添加 '''
        node = Node(item)
        node.next = self.head
        self.head = node
        node.next.prev = node

    def insert(self, pos, item):
        '''在链表的指定位置添加，这里以0为开始'''
        if pos < 0:
           self.add(item)
        elif pos > self.lenth() - 1:
           self.append(item)
        else:
            cur = self.head
            count = 0
            #循环找到要插入位置之前的一个
            while count < pos:
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        '''从链表中删除元素'''
        cur = self.head
        while cur != None:
            if cur.item == item:
                #判断是否是头结点
                if self.head == cur:
                    self.head = cur.next
                    if cur.next: #当不是只有一个元素的时候
                        self.head.prev = None
                    break
                else:
                    cur.prev.next = cur.next
                    if cur.next: #最后一个元素的话，就不用执行下面的语句了
                        cur.next.prev = cur.prev
                    break
            else:
                cur = cur.next

if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.lenth())
    dll.append(1)
    print(dll.is_empty())
    print(dll.lenth())
    dll.append(2)
    dll.add(5)
    dll.append(3)
    dll.append(4)
    dll.travl()
    dll.insert(2,100)
    dll.travl()
    dll.remove(3)
    dll.travl()
    dll.remove(5)
    dll.travl()
