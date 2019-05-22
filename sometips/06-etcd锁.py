# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   etcd_locker.py
@Time    :   2019/05/06 08:58:36
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import etcd
import time
from threading import Thread

def etcdlocker():
    """
        加锁的情况下，是一个个执行的，说明了etclock是实现了的
    """
    with etcd.Lock(client, 'mylock') as my_lock:
        print('获取到锁，正在执行操作..')
        time.sleep(1)
        print(time.ctime())
        my_lock.acquire(lock_ttl=60)

def noetcdlocker():
    """
        没有加锁的情况下，是同步执行的
    """
    print('正在执行操作..')
    time.sleep(1)
    print(time.ctime())

if __name__ == '__main__':
    client = etcd.Client(host='192.168.10.10',port=4001)
    for i in range(5):
        t = Thread(target=etcdlocker)
        t.start()
    