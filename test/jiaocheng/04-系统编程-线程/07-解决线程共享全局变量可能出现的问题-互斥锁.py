#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 02:31:45 PM CST

# File Name: 04-多线程使用全局变量.py
# Description:

"""

from threading import Thread, Lock
import time
#线程之间共享全局变量，进程之间是不共享的
g_num = 0

def test1():
    global g_num
    #这个线程和test2的线程会抢着上锁，如果有1方成功上锁，那么另一方会堵塞（一直等待）到这个锁被解开为止
    mutex.acquire() #获取锁，上锁
    for i in range(1000000):
        mutex.acquire() #获取锁，上锁
        g_num += 1
        mutex.release() #解锁，解锁后，其他堵塞中的线程会进行上锁
    mutex.release() #解锁，解锁后，其他堵塞中的线程会进行上锁
    print("---in test1 g_num is %d---"%g_num)

def test2():
    global g_num
    mutex.acquire() #获取锁，上锁
    for i in range(1000000): 
        #mutex.acquire() #最好把上锁解锁放在for里面，上锁的代码越少越好，因为上锁了，就成单线程了
        g_num += 1
        #mutex.release()
    mutex.release() #解锁，解锁后，其他堵塞中的线程会进行上锁

    print("---in test2 g_num is %d---"%g_num)

mutex = Lock() #创建一个锁

t = Thread(target=test1)
t.start()

#time.sleep(3)

t1 = Thread(target=test2)
t1.start()
print("---g_num=%d---"%g_num)

#当没有sleep的时候，2个线程同时在一个CPU上执行，那么就服从系统的进程管理，g_num+=1的执行是分2个步骤的，
#即g_num = g_num + 1，先执行右边的运算，再给左边赋值。当2个线程同时执行时，可能出现刚执行完右边的运算，
#就被系统搁置，转而执行另一个线程，执行完另一个线程时，回来在执行搁置的线程，这样就会出现问题。如果中间
#sleep 1s的话，等上一个进程执行完，再执行另一个进程，那么就不会出现问题了。

