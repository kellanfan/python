# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   redis_client.py
@Time    :   2020/03/02 15:19:57
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import redis
import etcd
import json
import sys
sys.path.append('../log')
from log.create_logger import create_logger

logger = create_logger()

def redis_client():
    try:
        etc_client = etcd.Client(host='etcd', port=2379)
        etc_result = etc_client.read('/python/info/redis')
        redis_info = json.loads(etc_result.value)
    except Exception as e:
        logger.error('Connect to Etcd server failed: [{}]'.format(e))
        return None
        

    try:
        redis_pool = redis.ConnectionPool(host=redis_info['host'],port=redis_info['port'])
        redis_conn = redis.Redis(connection_pool=redis_pool)
        return redis_conn
    except Exception as e:
        logger.error('Connect to Redis server [{0}] failed: [{1}]'.format(redis_info['host'],e))
        return None