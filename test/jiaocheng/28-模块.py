#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 29 Nov 2017 08:03:20 PM CST

# File Name: 28-模块.py
# Description: 模块其实就是py文件，也就是系统或者第三方甚至自己写好的python脚本，用于使用。

"""

#导入模块的方法
#第一种
import os
os.mkdir("aa")
os.rmdir("aa")
#第二种
#from os import mkdir,rmdir
#mkdir("aa") 不用写模块名了

def main():  #基本结构
    pass

if __name__ == '__main__': #这个的作用就是，如果直接执行这个脚本，那就可以执行，如果是调用就不会执行，方便测试等
    main()


'''
以后写代码的基本结构
class Xxx():
    pass

def xxx():
    pass

def main(): 这块就是程序的主框架
    pass

if __name__ == '__main__':
    main()
'''

