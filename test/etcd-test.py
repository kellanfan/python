#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 03 Dec 2018 02:48:46 PM CST

# File Name: etcd-test.py
# Description:

"""

import etcd
client = etcd.Client(host='127.0.0.1', port=4001)
client.write('/testkey', 'aaa')
result = client.read('/testkey')
print result.value
