# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   find_the_num.py
@Time    :   2019/05/13 16:31:49
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   math的使用
'''

# here put the import lib
import math

for num in range(1000):
    x = int(math.sqrt(num + 100))
    y = int(math.sqrt(num + 268))
    if ( x * x == num + 100) and (y * y == num + 268):
        print(num)
