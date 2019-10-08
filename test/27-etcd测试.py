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
import json
import etcd
client = etcd.Client(host='10.91.158.2', port=2379)
# data = json.dumps(data)
# client.write('/project/spiderman/postgres', data)
result = client.read('/project/spiderman/postgres')
a = json.loads(result.value)
print(a['host'])
