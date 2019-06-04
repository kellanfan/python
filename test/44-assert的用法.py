# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   err_assert.py
@Time    :   2019/06/03 15:28:41
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   assert的用法，assert 表达式 [, 参数]。
             assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题
'''

# here put the import lib

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    #类似于：
    #if n == 0:
    #   raise 'n is zero!'
    return 10 / n

def main():
    foo(0)
if __name__ == "__main__":
    main()