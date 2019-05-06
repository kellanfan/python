
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 18 Jan 2018 06:49:46 PM CST

# File Name: test.py
# Description: 导入模块的搜索路径

"""
import sys
print(sys.path)

sys.path.append('/home')
print(sys.path)

'''
模块循环导入问题，就是2个程序相互导入对方的模块，解决方法是有个主程序去调用，子程序之间不相互调用
'''
