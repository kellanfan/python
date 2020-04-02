# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   18-生成指定数量的随机数.py
@Time    :   2020/03/28 23:34:55
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import string
import random

def gen_uuid():
    uuid = ''.join(random.sample(string.ascii_lowercase + string.digits, 10))
    return uuid