#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 21 Jul 2017 04:52:07 PM CST

# File Name: thread-3-lock.py
# Description: 由于线程共享进程的变量，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。所以使用lock，使同一时间只能一个线程进行操作，其他线程等待，直到解锁。

"""

import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:   
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
