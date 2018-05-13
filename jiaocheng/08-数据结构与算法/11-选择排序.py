#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 10 May 2018 10:01:38 AM CST

# File Name: 11-选择排序.py
# Description: 把较小的换到前面

"""

def select_sort(alist):
    '''选择排序'''
    n = len(alist)
    for j in range(n-1):
        min_tar = j #这个相当于重置
        for i in range(j+1, n):
            if alist[min_tar] > alist[i]: #如果这个大，就把下标标记到对应的位置
                min_tar = i
        alist[j],alist[min_tar] = alist[min_tar],alist[j]


if __name__ == '__main__':
    l = [23,5,667,89,34,34,65,76]
    print(l)
    select_sort(l)
    print(l)
