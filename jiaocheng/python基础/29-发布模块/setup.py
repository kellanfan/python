#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 22 Apr 2019 10:38:22 AM CST

# File Name: setup.py
# Description:

"""
from setuptools import find_packages,setup
setup(
    name = 'kellan-test',
    version = '0.1',
    author = 'Kellan',
    author_email = 'kellan@kellan.com',
    description = 'A small example package',
    url = "www.kellantest.com",
    packages = find_packages()
            )
