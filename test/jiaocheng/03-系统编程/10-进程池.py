#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 11:52:51 AM CST

# File Name: 10-进程池.py
# Description:

"""
from multiprocessing import Pool
import os
import random
import time

def worker(num):
    for i in range(3):
        print('---pid=%d,task_id=%d'%(os.getpid(),num))
        time.sleep(random.randint(1,3))

mypool = Pool(3) #3表示进程池中最多有3个进程一起执行
                 #这个进程数不是越多越好，需要根据配置，进行压测得多
for i in range(10):
    print('---task_id=%d---'%i)
    #向进程池中添加任务
    #注意：如果添加的任务超过了进程池中的进程数（本次添加了10个任务），不会导致添加任务失败，
    #       未被执行的任务会等待之前的任务被进程执行完成后，自动添加到空闲的进程执行
    mypool.apply_async(worker,(i,)) #参数以元组形式添加进去
    #apply_async 这种是堵塞方式
mypool.close() #关闭进程池，不能再添加更多任务了
mypool.join() #主进程 创建、添加任务后，默认不会等待进程池中的任务执行完成后才结束，而是当主进程的工作完成后直接结束
              #如果这个地方没有阻塞（join），会导致进程池中的任务不会执行，这是因为进程池是在主进程中，主进程结束了，
              #进程池也就消失了
