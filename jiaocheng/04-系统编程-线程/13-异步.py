#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 08:18:29 PM CST

# File Name: 13-异步.py
# Description:

"""

from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

pool = Pool(3)
pool.apply_async(func=test,callback=test2)

#异步的理解：主进程正在做某件事情，突然　来了一件更需要立刻去做的事情，
#那么这种，在父进程去做某件事情的时候　并不知道是什么时候去做，的模式　就称为异步
while True:
    time.sleep(1)
    print("----主进程-pid=%d----"%os.getpid())

