#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 09 Jun 2017 01:57:21 PM CST

# File Name: qingcloudsdk.py
# Description:

"""
import qingcloud.iaas
import json
conn = qingcloud.iaas.connect_to_zone(
        'pek3a',
        'JKEDNDMVPAFWGXFTEAXL',
        'zUD7r8f1X8R28MHgKNOWUCm0NWD0WucyZv1H8aAg'
        )

def get_loadbalancer_id():
    ret = conn.describe_loadbalancers(status = ['active'])
    loadbalancer_id = []
    for lb in ret['loadbalancer_set']:
        loadbalancer_id.append(lb['loadbalancer_id'])
    return loadbalancer_id

def get_loadbalancer_status():
    lbid_list = get_loadbalancer_id()
    result = []
    result_dict = {}
    for lbid in lbid_list:
        ret = conn.describe_loadbalancer_backends(loadbalancer_id = lbid)
        a = ret['loadbalancer_backend_set'][0]
        result_dict['loadbalancer_id'] = a['loadbalancer_id']
        result_dict['loadbalancer_backend_id'] = a['loadbalancer_backend_id']
        result_dict['status'] = a['status']
        result.append(result_dict)
    return result

def get_instance_id():
    ret = conn.describe_instances(status = ['running'])
    instance_id = []
    for instance in ret['instance_set']:
        instance_id.append(instance['instance_id'])
    return instance_id


status = get_instance_id()
print status
