# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   27-etcd测试.py
@Time    :   2019/05/13 12:17:11
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import etcd
client = etcd.Client(host='192.168.10.10', port=4001)
client.write('/testkey', 'aaa')
result = client.read('/testkey')
print(result.value)
