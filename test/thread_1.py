#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print "I am listioning %s. %s" %(func, ctime())
        sleep(1)

def movie(func):
    for i in range(2):
        print "I am watching %s. %s" %(func, ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args=(u'东风破',))
t2 = threading.Thread(target=movie, args=(u'七里香',))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print "all over %s" %ctime()
