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
from collections import Counter

red = []
for _ in range(0,1000):
    red += sorted(random.sample(list(range(1,34)), 6))
red_num_counts = Counter(red)
true_red = []
for item in red_num_counts.most_common(6):
    true_red.append(item[0])


blue = []
for _ in range(0,1000):
    blue.append(random.randint(1,17))
blue_num_counts = Counter(blue)
true_blue = blue_num_counts.most_common(1)[0][0]

print("{} {}".format(sorted(true_red), true_blue))