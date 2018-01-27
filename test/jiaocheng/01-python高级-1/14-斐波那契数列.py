#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 27 Jan 2018 11:02:47 AM CST

# File Name: 14-斐波那契数列.py
# Description:

"""
def createnem():
    a,b = 0,1
    for i in range(500):
        yield b       #函数中一旦有yield，那这个就不是函数了，而变成了生成器，当执行的时候，遇到yield就会暂停执行，并将yield后面的值返回
        a,b = b,a+b

if __name__ == '__main__':
    a = createnem()
    for i in a: #生成器可以放在循环中，
        print(i)
#next(a)
#a.__next__()
#以上2中方式是一样的
