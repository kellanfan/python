#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 11 Apr 2018 04:23:47 PM CST

# File Name: m_time.py
# Description:

"""

import time

def application(env, start_reponse):
    status = 200
    headers = [
        ('Server', 'My Server')
    ]
    start_reponse(status, headers)
    return time.ctime()
