#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Sep 2017 06:37:57 PM CST

# File Name: 08-变量的补充.py
# Description:

"""
#我们现在知道Python的变量不是直接把值赋给了变量，而只是将变量指向内存的值。当这个值是数字或者字符串这种不可变量时，
#是没办法再次赋值的，只有可变值才能够直接改原来的值
#要注意，如果有全局变量，在函数中调用全局变量时，如果全局变量是可变的，那么就直接修改全局变量，如果是不可变的就新建一个局部变量
#例子1
a = 100
def test(num): #这时num也指向100
    num+=num #因为100是不可变的，所以这时得出的值是在另一个内存位置，并把num指向这个新值,这是个局部变量
    print num
test(a)
print a

#例子2
a1 = [100]
def test(num):
    num+=num #这里是直接改变了原来的值，因为list是可变的，
    print num
test(a1)
print a1

#例子3

a2 = [100]
def test(num):
    num=num+num #这里是把num指向了一个新值[100,100]
    print num
test(a2)
print a2
