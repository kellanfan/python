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
p.join(1)#堵塞
# 是否等待进程实例执行结束，或等待多少秒，join中的1是timeout值
print("----main----")
