#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 08:09:16 PM CST

# File Name: 12-Threadlocal.py
# Description: 如果有多层函数调用的情况下，传数据的方式有2中,1是把变量当做参数,2是设置全局变量
                全局变量会被线程相互影响,为了不相互影响,可以使用全局字典,但是这样代码不好看,所以
                引用了Threadlocal类,这是一个特殊的类,创建的对象的同一个属性,在不同的线程调用时
                不会相互影响

"""

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()
