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

def get_instance():
    ret = conn.describe_instances(status = ['running'])
    instances_info = []
    for instance in ret['instance_set']:
        instance_info = {} #每次循环要新建一个字典，如果在循环外，每次循环使用的是同一个字典，因为key值一样，导致value值被下次循环覆盖，所以最后的list的所有值都是最后一次循环的值
        instance_info['instance_id'] = instance['instance_id']
        instance_info['ip'] = instance['vxnets'][0]['private_ip']
        instances_info.append(instance_info)
    return instances_info
if __name__ == "__main__":
    infos = get_instance()
    for i in infos:
        print "the ip of %s is %s..." %(i['instance_id'], i['ip'])
