#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 02 Apr 2019 07:09:01 AM CST

# File Name: map_process.py
# Description:

"""

from multiprocessing.dummy import Pool
import requests
import datetime

urls = [
    'http://www.baidu.com',
    'http://www.python.org',
    'http://docs.python-requests.org/zh_CN/latest/user/quickstart.html',
    'http://www.wufazhuce.com/',
    'http://wiki.python.org/moin/',
    'http://www.python.org/doc/',
    'http://www.python.org/psf/',
    'http://planet.python.org/',
    'http://www.python.org/download/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'http://www.python.org/about/'
    ]
starttime = datetime.datetime.now()
pool = Pool(10)
result = pool.map(requests.get, urls)
print(result)
pool.close()
pool.join()
print((datetime.datetime.now() - starttime).seconds)
