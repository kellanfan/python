#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 08 Feb 2018 04:35:36 PM CST

# File Name: 07-pdb调试.py
# Description:

"""

#使用pdb调试
#python(3) -m pdb xxx.py
#还可以埋点
#import pdb
#pdb.set_trace() 在要调试的代码上一行，类似于b的功能

#相关命令：
#l ----- list 显示当前代码
#n ----- next 向下执行一行代码
#c ----- continue 继续执行代码，不遇到是程序停止的代码，会一直执行完剩余代码
#b ----- break 添加断点 b 7 添加到第7行，添加后要执行c到断点，可以添加多个断点。
#clear ---  删除断点，clear 断点序号
#s ----- step 如果指针指向的行是个函数的引用，按s可以跳到函数中，查看函数中的执行情况
#p ----- print 打印函数一个变量的值
#a ----- args 打印所有的形参数据
#r ----- return 快速执行到函数的最后一行
#q ----- quit 退出调试


#日志调试
#print。。。。。
