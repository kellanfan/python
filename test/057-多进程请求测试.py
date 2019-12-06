# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   057-多进程请求测试.py
@Time    :   2019/12/06 09:04:26
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import os
import time
import random
import requests
from multiprocessing import Pool
import sys
sys.path.append('/root/totoro/log')


def worker():
    while True:
        ret = requests.get('http://192.168.1.5:8899')
        print('pid:{},status_code:{}'.format(os.getpid(),ret.status_code))
        time.sleep(random.randint(1,3))
mypool = Pool(10)
for _ in range(10):
	mypool.apply_async(worker)

mypool.close()
mypool.join()