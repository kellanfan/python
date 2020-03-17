# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   bots.py
@Time    :   2020/03/17 13:08:57
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
class Describe_Bots(object):
    def __init__(self, zone, offset='0'):
        self.__data = { 
            'action':'DescribeBots',
            'limit':'100',
            'offset': offset,
            'zone': zone
            }

    def __call__(self):
        return self.__data