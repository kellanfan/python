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
from hypernode import Describe_Bots


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
                #try:
                #    self.__mem_oversale_rate = compute_server_conf['compute_server']['mem_oversale_rate']
                #except:
                #    self.__mem_oversale_rate = 1
                try:
                    self.__disk_reserve_rate = compute_server_conf['compute_server']['disk_reserve_rate']
                except:
                    self.__disk_reserve_rate = 0.2

    def cal_data(self):
        real_cpu = 0; real_mem = 0; real_disk = 0
        vcpu = 0; vmem = 0; vdisk = 0; 
        used_vcpu = 0; used_vmem = 0; used_vdisk = 0
        per_cpu = 0; per_mem = 0 ; per_disk = 0
        for hypernode in self.__content:
            host_machine = hypernode['host_machine']
            status = hypernode['status']
            if status not in ['active', 'standby']:
                print "\033[0;31m%s status is %s!!! Maybe broken, please check!!! \033[0m" %(host_machine, status)
                continue
            try:
                place_group_ids = hypernode['place_group_id_bak']
            except:
                print "%s info cannot get!!!" %host_machine
                continue
            if place_group_ids == self.__plg:
                self.__hyper_list.append(host_machine)
                real_cpu += hypernode['total_vcpu']/self.__cpu_oversale_rate
                real_mem += hypernode['real_total_memory']
                real_disk += hypernode['used_disk'] + hypernode['free_disk']
                vcpu += hypernode['total_vcpu']
                vmem += hypernode['total_memory']
                vdisk += (hypernode['used_disk'] + hypernode['free_disk'])
                used_vcpu += hypernode['used_vcpu']
                used_vmem += hypernode['used_memory']
                used_vdisk += hypernode['virtual_disk']
                per_cpu += (100 - hypernode['cpu_idle'])
                per_mem += int((1 - float(hypernode['real_free_memory'])/ float(hypernode['real_total_memory']))*100)
                per_disk += int((float(hypernode['used_disk']) / float(real_disk))*100)

        result = []
        lenth = len(self.__hyper_list)
        if vcpu == 0 or vmem == 0 or vdisk == 0:
            return result
        else:
            real_mem = int(real_mem/1024)
            real_disk = int(real_disk/1024/1024)
            vmem = int(vmem/1024)
            vdisk = int(vdisk/self.__disk_reserve_rate/1024/1024)
            used_vmem = int(used_vmem/1024)
            used_vdisk = int(used_vdisk/1024/1024)
            free_vcpu = vcpu - used_vcpu
            free_vmem = vmem - used_vmem
            free_vdisk = vdisk - used_vdisk
            per_cpu = int(float(per_cpu) / float(lenth))
            per_mem = int(float(per_mem) / float(lenth))
            per_disk = int(float(per_disk) / float(lenth))
            per_vcpu = int((float(used_vcpu)/float(vcpu))*100)
            per_vmem = int((float(used_vmem)/float(vmem))*100)
            per_vdisk = int((float(used_vdisk)/float(vdisk))*100)
            
            result.append(str(real_cpu) + 'C')
            result.append(str(real_mem) + 'G')
            result.append(str(real_disk) + 'T')
            result.append(per_cpu)
            result.append(per_mem)
            result.append(per_disk)
            result.append(str(vcpu) + 'C')
            result.append(str(vmem) + 'G')
            result.append(str(vdisk) + 'T')
            result.append(str(used_vcpu) + 'C')
            result.append(str(used_vmem) + 'G')
            result.append(str(used_vdisk) + 'T')
            result.append(str(free_vcpu) + 'C')
            result.append(str(free_vmem) + 'G')
            result.append(str(free_vdisk) + 'T') 
            result.append(int(per_vcpu))
            result.append(int(per_vmem))
            result.append(int(per_vdisk))
            return result, lenth

def main():
    url = 'http://api.qcdemo.com:7777/iaas/'
    zone = 'demo1'
    bots = Describe_Bots(zone,url)
    content = bots.run()
    total_hyper = content['total_count']
    if total_hyper > 100:
        content1 = Describe_Bots(zone, url, '100')
        content_botset = content1['bot_set'] + content['bot_set']
    else:
        content_botset = content['bot_set']

    sas = HyperData(content_botset, 'plg-00000000')
    print sas.cal_data()

if __name__ == '__main__':
    main()

