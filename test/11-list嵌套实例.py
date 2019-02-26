#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 26 Feb 2019 10:13:51 PM CST

# File Name: 11-list嵌套实例.py
# Description: 一个学校，有3个办公室，现在有8位教师等待工位的分配，请编写程序，完
成随机的分配

"""
import random
#创建3个办公室的list和代表8位老师的list
offices = [[],[],[]]
teachers = [1,2,3,4,5,6,7,8]


for teacher in teachers:
    index = random.randint(0,2)
    offices[index].append(teacher)
i=0
for office in offices:
    print('办公室%d的人数为%d'%(i,len(office)))
    i += 1
    for teacher in office:
        print('%s '%teacher,end='')
    print('\n')

