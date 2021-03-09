#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 19 Aug 2018 10:19:14 PM CST

# File Name: resource.py
# Description:

"""
import yaml
import time
import os, sys

class HyperData(object):
    def __init__(self, content, plg):
        self.__content = content
        self.__plg = plg
        self.__get_config()
        self.__hyper_list = []

    def __get_config(self):
        conf_file = '/pitrix/conf/global/server.yaml'
        if os.path.exists(conf_file):
            with open(conf_file) as f:
                compute_server_conf = yaml.load(f.read())
                try:
                    self.__cpu_oversale_rate = compute_server_conf['compute_server']['cpu_oversale_rate']
                except:
                    self.__cpu_oversale_rate = 5
                try:
                    self.__mem_oversale_rate = compute_server_conf['compute_server']['mem_oversale_rate']
                except:
                    self.__mem_oversale_rate = 1
                try:
                    self.__disk_reserve_rate = compute_server_conf['compute_server']['disk_reserve_rate']
                except:
                    self.__disk_reserve_rate = 0.2
        else:
            self.__cpu_oversale_rate = 5
            self.__mem_oversale_rate = 1
            self.__disk_reserve_rate = 0.2

    def cal_data(self):
        real_cpu = 0; real_mem = 0; real_disk = 0; real_used_disk = 0; real_used_mem = 0
        vcpu = 0; vmem = 0; vdisk = 0
        used_vcpu = 0; used_vmem = 0; used_vdisk = 0
        per_cpu = 0; per_mem = 0 ; per_disk = 0
        for hypernode in self.__content:
            host_machine = hypernode['host_machine']
            if hypernode['status'] not in ['active', 'standby']:
                continue
            
            if not hypernode.has_key('real_total_memory'):
                continue
 
            if hypernode['place_groups'][0]['place_group_id'] == self.__plg:
                self.__hyper_list.append(host_machine)
                real_cpu += hypernode['total_vcpu']/self.__cpu_oversale_rate
                real_mem += hypernode['real_total_memory']
                real_used_mem += hypernode['real_used_memory']
                real_used_disk += hypernode['used_disk']
                real_disk += hypernode['used_disk'] + hypernode['free_disk']
                vcpu += hypernode['total_vcpu']
                vmem += hypernode['total_memory']
                vdisk += (hypernode['used_disk'] + hypernode['free_disk'])
                used_vcpu += hypernode['used_vcpu']
                used_vmem += hypernode['used_memory']
                used_vdisk += hypernode['virtual_disk']
                per_cpu += (100 - hypernode['cpu_idle'])
                per_mem += (1 - float(hypernode['real_free_memory'])/ float(hypernode['real_total_memory']))*100
                
        result = []
        lenth = len(self.__hyper_list)
        if not all([vcpu,vmem,vdisk]):
            return (0,result)
        else:
            per_mem = (float(real_used_mem)/float(real_mem))*100
            real_mem = int(real_mem/1024)
            per_disk = (float(real_used_disk)/float(real_disk))*100
            real_disk = int(real_disk/1024/1024)
            per_cpu = float(per_cpu) / float(lenth)
            
            vmem = int(vmem/1024)
            vdisk = int(vdisk/self.__disk_reserve_rate/1024/1024)
            used_vmem = int(used_vmem/1024)
            used_vdisk = int(used_vdisk/1024/1024)
            free_vcpu = vcpu - used_vcpu
            free_vmem = vmem - used_vmem
            free_vdisk = vdisk - used_vdisk
            per_vcpu = (float(used_vcpu)/float(vcpu))*100
            per_vmem = (float(used_vmem)/float(vmem))*100
            per_vdisk = (float(used_vdisk)/float(vdisk))*100
           
            result.append(str(real_cpu) + 'C')
            result.append(str(real_mem) + 'G')
            result.append(str(real_disk) + 'T')
            result.append('{:.2f}'.format(per_cpu))
            result.append('{:.2f}'.format(per_mem))
            result.append('{:.2f}'.format(per_disk))
            result.append(str(vcpu) + 'C')
            result.append(str(vmem) + 'G')
            result.append(str(vdisk) + 'T')
            result.append(str(used_vcpu) + 'C')
            result.append(str(used_vmem) + 'G')
            result.append(str(used_vdisk) + 'T')
            result.append(str(free_vcpu) + 'C')
            result.append(str(free_vmem) + 'G')
            result.append(str(free_vdisk) + 'T') 
            result.append('{:.2f}'.format(per_vcpu))
            result.append('{:.2f}'.format(per_vmem))
            result.append('{:.2f}'.format(per_vdisk))
            return lenth,result