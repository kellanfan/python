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

t = test()
#第一次运行只能使用next或者send(None)
print(t.__next__())
#send的作用相当于使生成器继续运行，并且传递的参数为yield的返回值(程序中即temp的值)
print(t.send("Hello World"))
print(t.__next__())#相当于send(None) 此时temp = None
