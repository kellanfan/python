#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 06:03:07 PM CST

# File Name: 09-死锁及解决方法.py
# Description:

"""
#解决方法
#1.设置超时时间，mutexB.acquire(2),在2s内没有锁上就超时，直接过去
#2.银行家算法
from threading import Lock
import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire(): #对mutexA这个锁进行上锁
            print(self.name+'--do1---up---')
            time.sleep(1)

            #这里和下面的相互等待对方释放锁，然后上锁，但是这是不可能的，产生死锁
            if mutexB.acquire():  
                print(self.name+'--do1---down---')
                mutexB.release()

            mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        if mutexB.acquire(): #对mutexB这个锁进行上锁
            print(self.name+'--do2---up---')
            time.sleep(1)

            if mutexA.acquire():
                print(self.name+'--do2---down---')
                mutexA.release()

            mutexB.release()

if __name__ == '__main__':
    mutexA = threading.Lock()
    mutexB = threading.Lock()
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
