#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 07 Mar 2018 01:59:39 PM CST

# File Name: 02-使用线程的第二种方法.py
# Description:

"""

import threading
import time
#执行顺序不一定，系统调度决定
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name+ '@' + str(i) #name属性中保存的是当前线程的名字
            print(msg)
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
