#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 27 Jan 2018 12:20:29 PM CST

# File Name: 15-send.py
# Description:

"""
def test():
    i = 0
    while i < 5:
        tmp = yield i #当执行到yield的时候停止，再次执行时需要给tmp赋值，但是yield这是已经没有值可以赋给tmp，所以返回None
        print(tmp)
        i += 1

a = test()
a.send(None) #send的作用就是将这个值发送给tmp,如果第一次就使用send的话，程序会崩，因为第一次没有tmp可以接收，所以第一次可以先传个None，a.send(None)

