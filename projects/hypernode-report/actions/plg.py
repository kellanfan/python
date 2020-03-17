# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   plg.py
@Time    :   2020/03/17 13:08:52
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
class Plg(object):
    def __init__(self, zone):
        self.__data = {
            'action': 'DescribePlaceGroups',
            'status': 'available',
            'zone': zone
        }

    def __call__(self):
        return self.__data