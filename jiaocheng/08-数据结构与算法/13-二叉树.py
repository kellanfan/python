#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 17 May 2018 03:33:25 PM CST

# File Name: 13-二叉树.py
# Description:

"""
class Node(object):
    def __init__(self, item):
        self.item = item
        self.lson = None
        self.rson = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        queue = [self.root]
        if self.root is None:
            self.root = node
            return
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lson is None:
                cur_node.lson = node
                return
            else:
                queue.append(cur_node.lson)

            if cur_node.rson is None:
                cur_node.rson = node
                return
            else:
                queue.append(cur_node.rson)

    def broad_travel(self):
        queue = [self.root]
        if self.root is None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.lson:
                queue.append(cur_node.lson)
            if cur_node.rson:
                queue.append(cur_node.rson)

    def preorder(self, node):
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.lson)
        self.preorder(node.rson)

    def inorder(self, node):
        if node is None:
            return

        self.inorder(node.lson)
        print(node.item, end=' ')
        self.inorder(node.rson)

    def postorder(self, node):
        if node is None:
            return

        self.postorder(node.lson)
        self.postorder(node.rson)
        print(node.item, end=' ')

if __name__ ==  '__main__':
    t = Tree()
    for i in range(9):
        t.add(i)
    t.broad_travel()
    print(' ')
    t.preorder(t.root)
    print(' ')
    t.inorder(t.root)
    print(' ')
    t.postorder(t.root)
    print(' ')
