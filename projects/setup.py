#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 22 Apr 2019 11:09:20 AM CST

# File Name: setup.py
# Description:

"""
from setuptools import setup, find_packages
setup(name='hyperreport',
      version='0.1',
      description='hyper resource report by API', 
      author='Kellan Fan', 
      author_email = 'fankai@yunify.com',
      url = 'Null',
      packages = find_packages(),
      package_data = {
      '':['*.yml'],
      }
)
