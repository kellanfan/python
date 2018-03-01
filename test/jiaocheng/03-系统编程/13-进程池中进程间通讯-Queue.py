#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 02:57:04 PM CST

# File Name: 12-进程间通讯-Queue.py
# Description:

"""

from multiprocessing import Pool, Manager
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
    print("%s start"%os.getpid())
    q = Manager().Queue() #使用Manager中的Queue来初始化
    mypool = Pool()
    mypool.apply(write, (q,)) #使用阻塞式创建进程，以防没写完就读了
    mypool.apply(read, (q,))
    mypool.close()
    mypool.join()
    print("%s stop"%os.getpid())
    print('\n所有数据读写完成')
    read(q)

if __name__ == '__main__':
    main()

