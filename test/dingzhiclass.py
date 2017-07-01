#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 01 Jul 2017 05:27:14 PM CST

# File Name: dingzhiclass.py
# Description:

"""

class Student(object):
    def __init__(self, name):
        self.name = name

print Student('kellan')

class Student_str(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name

print Student_str('kellan')

s = Student_str('kellan')
print s

