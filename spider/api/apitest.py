#!/usr/bin/env python
#coding=utf8
#from lib.getcontent import getcontent
from getcontent import getcontent
zonelist = ['prod2', 'test', 'test2', 'tkwh']
for zone in zonelist:
    content = getcontent(zone)
    hyper_sas = []
    hyper_ssd = []
    hyper_sata = []
    hyper_other = []
    total_hyper =  content['total_count']
    for hypernode in content['bot_set']:
        host_machine = hypernode['host_machine']
        if zone == 'test':
            place_group_ids = hypernode['place_groups'][0]['place_group_id']
        else:
            place_group_ids = hypernode['place_group_ids'][0]
        
        if place_group_ids == 'plg-00000000':
            hyper_sas.append(host_machine)
        elif place_group_ids == 'plg-00000001':
            hyper_ssd.append(host_machine)
        elif place_group_ids == 'plg-00000002':
            hyper_sata.append(host_machine)
        else:
            hyper_other.append(host_machine)
    
    lenth_sas = len(hyper_sas)
    lenth_ssd = len(hyper_ssd)
    lenth_sata = len(hyper_sata)
    lenth_other = len(hyper_other)
    
    print "zone: %s\ntotal: %d, sas: %d, ssd: %d, sata: %d, other: %d" %(zone, total_hyper, lenth_sas, lenth_ssd, lenth_sata, lenth_other)
