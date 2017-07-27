#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 26 Jul 2017 08:21:57 PM CST

# File Name: taskworker.py
# Description:

"""

import Queue, time, sys
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager
class Queuemanager(BaseManager):
    pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
# 这块不是很明白，manager已经注册了，为什么还要注册？？？
Queuemanager.register('send_task_queue')
Queuemanager.register('get_task_queue')
#连接到manager server
server_address = '127.0.0.1'
print 'connect to server %s...' %server_address
# 端口和验证码注意保持与taskmanager.py设置的完全一致:
m = Queuemanager(address=(server_address,6666), authkey=123456)
#从网络连接到server
m.connect()
#获取Queue对象
send = m.send_task_queue()
get = m.get_task_queue()
# 从task队列取任务,并把结果写入result队列
for i in range(10):
    try:
        n = send.get(timeout=1)
        print 'running %d * %d ' %(n, n)
        r = '%d * %d = %d' %(n, n, n*n)
        time.sleep(1) #每取一个数，sleep 1s 要不过程太快
        get.put(r)
    except Queue.Empty:    #当取完最后一个数后，要做相应的处理
        print 'task queue is empty...'
#处理结束
print 'woker done...'
