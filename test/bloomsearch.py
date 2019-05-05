
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 05 Dec 2017 11:09:51 AM CST

# File Name: bloomsearch.py
# Description:

"""
class Bloomfolter(object):
    def __init__(self,size):
        self.values = [False] * size
        self.size = size

    def hash_value(self, value):
        return hash(value) % self.size

    def add_value(self, value):
        h = self.hash_value(value)
        self.values[h] = True

    def might_contain(self, value):
        h = self.hash_value(value)
        return self.values[h]

    def print_contents(self):
        print(self.values)

