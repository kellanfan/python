# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   prod.py
@Time    :   2019/05/13 11:54:14
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
from functools import reduce

def prod(l):
    return reduce(lambda x,y:x*y, map(int, l))
L = '12345667'
a = prod(L)
print(a)
