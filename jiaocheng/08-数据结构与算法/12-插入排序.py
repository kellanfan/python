#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 13 May 2018 05:14:27 PM CST

# File Name: 12-插入排序.py
# Description:

"""

def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        i = j #i代表内层循环的起始值
        #for i in range(j, 0, -1) #从j开始，每次递减1
        while i > 0: #从无序序列中取出一个元素，即i位置元素然后将其插入前面正确的位置中
            if alist[i] < alist[i-1]: #和前面的元素做对比
                alist[i], alist[i-1] = alist[i-1], alist[i] #如果小，就交换
                i -= 1  #i-1后的i还是代表之前的那个元素
            else:
                break #如果比前面的元素大，那么就已经在正确位置了，就退出循环

if __name__ == '__main__':
    l = [33, 42, 34, 74, 65, 67, 34, 46]
    insert_sort(l)
    print(l)
