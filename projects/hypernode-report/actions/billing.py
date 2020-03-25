#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Wed 25 Mar 2020 07:27:47 PM CST

# File Name: billing.py
# Description:

"""
class Billing(object):
    def __init__(self, zone='pek3a',start_time=None,end_time=None):
        self.__data = {
            'action': 'GetChargeRecords',
            'zone': zone,
        } 
        self.start_time = start_time
        self.end_time = end_time

    def __call__(self):
        if self.start_time is not None:
            self.__data['start_time'] = self.start_time
        if self.end_time is not None:
            self.__data['end_time'] = self.end_time
        return self.__data
