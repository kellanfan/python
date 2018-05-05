#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 28 Apr 2018 02:02:08 PM CST

# File Name: 03-效率测试.py
# Description:

"""

from timeit import Timer

def t1():
    l = []
    for i in range(10000):
        l.append(i)

def t2():
    l = []
    for i in range(10000):
        l += [i]

def t3():
    l = []
    for i in range(10000):
        l.insert(0,i)

def t4():
    l = [i for i in range(10000)]

def t5():
    l = []
    for i in range(10000):
        l.extend([i])

def t6():
    l = list(range(10000))


timer1 = Timer("t1", "from __main__ import t1")
print("append: %s" %timer1.timeit(1000))
timer2 = Timer("t2", "from __main__ import t2")
print("+: %s" %timer2.timeit(1000))
timer3 = Timer("t3", "from __main__ import t3")
print("insert: %s" %timer3.timeit(1000))
timer4 = Timer("t4", "from __main__ import t4")
print("[i for i in range(10000)]: %s" %timer4.timeit(1000))
timer5 = Timer("t5", "from __main__ import t5")
print("extend: %s" %timer5.timeit(1000))
timer6 = Timer("t6", "from __main__ import t6")
print("list: %s" %timer6.timeit(1000))


#说明
#python的list采用分离式动态顺序表，而且存储数据部分存储的只是具体数据的地址，实际的数据是存储在别的地方
#扩容时加4倍，达到阈值50000的之后，加1倍
