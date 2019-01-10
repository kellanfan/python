#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 10 Jan 2019 11:30:07 AM CST

# File Name: 02-doctest模块测试.py
# Description: doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。
               也可以这样使用python -m doctest -v xxx.py
               如果不想将doctest测试用例嵌入到python的源码中，则可以建立一个独立的文本文件来保存测试用例。 
               将doctest测试用例从python源码中剥离出来放到xxx.txt文件里。python -m doctest -v xxx.txt
"""

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True) 
    #verbose参数，如果设置为True则在执行测试的时候会输出详细信息。默认是False，表示运行测试时，只有失败的用例会输出详细信息，成功的测试用例不会输入任何信息。
