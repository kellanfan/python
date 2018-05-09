#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 07 May 2018 09:12:35 AM CST

# File Name: 10-冒泡排序.py
# Description:

"""
def alist_sort(alist):
    n = len(alist)
    for i in range(0, n-1): #共要从头走多少次
        for j in range(0, n-1-i): #这次要对比多少次
            count = 0
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            return

if __name__ == '__main__':
    l = [23,55,22,767,9,2,6]
    print(l)
    alist_sort(l)
    print(l)
