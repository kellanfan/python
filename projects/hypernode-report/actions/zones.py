# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   zones.py
@Time    :   2020/03/17 12:45:54
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
class Zones(object):
    def __init__(self, status='active'):
        self.__data = {
            'action': 'DescribeZones',
            'status': status
        } 

    def __call__(self):
        return self.__data