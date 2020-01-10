# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   机选双色球.py
@Time    :   2020/01/11 00:15:05
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import random
number = sorted(random.sample(list(range(1,34)), 6))
blue = random.randint(1,17)
number.append(blue)
print(number)