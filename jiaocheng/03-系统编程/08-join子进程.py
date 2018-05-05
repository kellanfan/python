#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Feb 2018 04:10:28 PM CST

# File Name: 08-join子进程.py
# Description:

"""

from multiprocessing import Process
import time
import random

def test():
    for i in range(random.randint(1,5)):
        print("----%d---"%i)
        time.sleep(1)

p = Process(target=test)
p.start()
p.join()#堵塞,如果无参数，那么就是等所有子进程都结束，主进程才会结束
# 是否等待进程实例执行结束，或等待多少秒，join中的1是timeout值
print("----main----")
