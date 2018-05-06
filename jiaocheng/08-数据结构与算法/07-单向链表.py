#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 04 May 2018 01:57:25 PM CST

# File Name: 07-单向链表.py
# Description:

"""
from Linklist import LinkList

class Node(object):
    '''节点'''
    def __init__(self, item):
        self.item = item
        self.next = None

class Singelink(LinkList):
    '''单向链表'''
    def append(self, item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        '''链表头部添加
        要做的就是将新加的node的next指向原来的下一个node，而head指向新加的node   
        '''
        node = Node(item)
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

    def remove(self, item):
        '''从链表中删除元素'''
        cur = self.head
        pre = None
        while cur != None:
            if cur.item == item:
                #判断是否是头结点
                if self.head == cur:
                    self.head = cur.next
                    break
                else:
                    pre.next = cur.next
                    break
            else:
                #跳到下一个节点，先移动pre才能移动cur
                pre = cur
                cur = cur.next


if __name__ == '__main__':
    ll = Singelink()
    print(ll.is_empty())
    print(ll.lenth())
    ll.append(1)
    print(ll.is_empty())
    print(ll.lenth())
    ll.append(2)
    ll.add(8) # 8 1 2 3 4 5 6
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travl()
    ll.insert(-1, 9) # 9 8 1 2 3 4 5 6
    ll.travl()
    ll.insert(3, 100) # 9 8 1 100 2 3 4 5 6
    ll.travl()
    ll.insert(10, 200) #9 8 1 100 2 3 4 5 6 200
    ll.travl()
    ll.remove(100)
    ll.travl()
    ll.remove(9)
    ll.travl()
    ll.remove(200)
    ll.travl()
    print(ll.search(3))

