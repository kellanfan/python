#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 02:57:04 PM CST

# File Name: 12-进程间通讯-Queue.py
# Description:

"""

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    for i in range(1,4):
        print("put %d to queue"%i)
        q.put(i)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            print("get %d from queue"%q.get())
            time.sleep(random.random())
        else:
            break

def main():
    q = Queue() #父进程创建Queue，并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start() #启动子进程pw
    pw.join() #等待子进程结束
    pr.start()
    pr.join()
    print('\n所有数据读写完成')
    read(q)

if __name__ == '__main__':
    main()

