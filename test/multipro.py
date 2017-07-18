#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 18 Jul 2017 08:14:59 PM CST

# File Name: multipro.py
# Description:

"""

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
