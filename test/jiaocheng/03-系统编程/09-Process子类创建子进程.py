#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 11:20:41 AM CST

# File Name: 09-Process子类创建子进程.py
# Description:

"""

from multiprocessing import Process
import time

class MyProcess(Process):
    def run(self):
        self.test()

    def test(self):
        while True:
            print('---sub---')
            time.sleep(1)

p = MyProcess() #这种创建子进程的方法比之前会简便易一些
p.start() #start函数在Process父类中调用run方法

while True:
    print('---main---')
    time.sleep(1)

    

