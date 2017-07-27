#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 26 Jul 2017 08:06:51 PM CST

# File Name: taskmanager.py
# Description:

"""
#加载random产生随机数，time模块用于sleep时间，Queue产生队列
import random, time, Queue
from multiprocessing.managers import BaseManager
#创建2个queue对象，一个队列用于manager将数据写进，worker从这个队列获取数据在进行指定的处理，另一队列的作用是将worker产生的结果写到这个队列，以便读取
send_task_queue = Queue.Queue()
get_task_queue = Queue.Queue()
## 从BaseManager继承的QueueManager
class Queuemanager(BaseManager): #这里可以尝试直接使用BaseManager，应该没有关系的
    pass
#将2个队列注册到网络，callable参数关联了Queue对象
Queuemanager.register('send_task_queue', callable=lambda: send_task_queue)
Queuemanager.register('get_task_queue', callable=lambda: get_task_queue)
#绑定端口，设置验证码
manager = Queuemanager(address=('', 6666), authkey='123456')
#启动Queue
manager.start()
#获得通过网络访问的Queue对象: 在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
send = manager.send_task_queue()
get = manager.get_task_queue()
#放数据进去
for i in range(10):
    n = random.randint(0,1000) #产生随机整数，放进Queue
    print "put task %d.." %n
    send.put(n)
#从第二的产生结果的Queue中获取结果,如果worker一直没有数据，那么10s后退出，这就是timeout的作用
print 'try to get result...'
for i in range(10):
    r = get.get(timeout=10)
    print 'Result: %s' %r
#关闭
manager.shutdown()
