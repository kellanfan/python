#!/usr/bin/python
from getcontent import Describe_Bots
import openpyxl, time
import os
zonelist = ['prod2', 'test', 'test2', 'tkwh']
dt = time.strftime('%Y-%m-%d')

def insertwb(ws,result):
    col = [2,4,5,6,7]
    i = 0
    if result:
        for c in col:
            for row in range(2, 5):
                ws.cell(row=row, column=c).value = result[i]
                i += 1

def cal_data(all_total_real_cpu, all_total_real_mem, all_total_real_disk, all_total_vcpu, all_total_vmem, all_total_vdisk, all_total_used_vcpu, all_total_used_vmem, all_total_used_vdisk):
    result = []
    if all_total_vcpu == 0 or all_total_vmem == 0 or all_total_vdisk == 0:
        return result
    else:
        all_total_real_mem = int(all_total_real_mem/1024)
        all_total_real_disk = int(all_total_real_disk/1024/1024)
        all_total_vmem = int(all_total_vmem/1024)
        all_total_vdisk = int(all_total_vdisk/1024/1024)
        all_total_used_vmem = int(all_total_used_vmem/1024)
        all_total_used_vdisk = int(all_total_used_vdisk/1024/1024)
        all_total_free_vcpu = all_total_vcpu - all_total_used_vcpu
        all_total_free_vmem = all_total_vmem - all_total_used_vmem
        all_total_free_vdisk = all_total_vdisk - all_total_used_vdisk
        percent_vcpu = (float(all_total_used_vcpu)/float(all_total_vcpu))*100
        percent_vmem = (float(all_total_used_vmem)/float(all_total_vmem))*100
        percent_vdisk = (float(all_total_used_vdisk)/float(all_total_vdisk))*100
        result.append(str(all_total_real_cpu) + 'C')
        result.append(str(all_total_real_mem) + 'G')
        result.append(str(all_total_real_disk) + 'T')
        result.append(str(all_total_vcpu) + 'C')
        result.append(str(all_total_vmem) + 'G')
        result.append(str(all_total_vdisk) + 'T')
        result.append(str(all_total_used_vcpu) + 'C')
        result.append(str(all_total_used_vmem) + 'G')
        result.append(str(all_total_used_vdisk) + 'T')
        result.append(str(all_total_free_vcpu) + 'C')
        result.append(str(all_total_free_vmem) + 'G')
        result.append(str(all_total_free_vdisk) + 'T') 
        result.append(str(int(percent_vcpu)) + 'C')
        result.append(str(int(percent_vmem)) + 'G')
        result.append(str(int(percent_vdisk)) + 'T')
        return result


for zone in zonelist:
    wb = openpyxl.load_workbook('result.xlsx')
    content = Describe_Bots(zone)
    total_hyper = content['total_count']
    sas_result = []
    ssd_result = []
    sata_result = []
    hyper_sas = []
    hyper_ssd = []
    hyper_sata = []
    hyper_other = []
    all_total_sas_vcpu = 0
    all_total_ssd_vcpu = 0
    all_total_sata_vcpu = 0
    all_total_sas_vmem = 0
    all_total_ssd_vmem = 0
    all_total_sata_vmem = 0
    all_total_sas_vdisk = 0
    all_total_ssd_vdisk = 0
    all_total_sata_vdisk = 0
    all_total_used_sas_vcpu = 0
    all_total_used_ssd_vcpu = 0
    all_total_used_sata_vcpu = 0
    all_total_used_sas_vmem = 0
    all_total_used_ssd_vmem = 0
    all_total_used_sata_vmem = 0
    all_total_used_sas_vdisk = 0
    all_total_used_ssd_vdisk = 0
    all_total_used_sata_vdisk = 0
    all_total_real_sas_cpu = 0
    all_total_real_sas_mem = 0
    all_total_real_sas_disk = 0
    all_total_real_ssd_cpu = 0
    all_total_real_ssd_mem = 0
    all_total_real_ssd_disk = 0
    all_total_real_sata_cpu = 0
    all_total_real_sata_mem = 0
    all_total_real_sata_disk = 0
    for hypernode in content['bot_set']:
        host_machine = hypernode['host_machine']
        place_group_ids = hypernode['place_groups'][0]['place_group_id']
    
        if place_group_ids == 'plg-00000000':
            hyper_sas.append(host_machine)
            total_real_sas_cpu = hypernode['total_vcpu']/5
            all_total_real_sas_cpu = all_total_real_sas_cpu + total_real_sas_cpu
            all_total_real_sas_mem = all_total_real_sas_mem + hypernode['real_total_memory']
            total_real_sas_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_real_sas_disk = all_total_real_sas_disk + total_real_sas_disk
            all_total_sas_vcpu = all_total_sas_vcpu + hypernode['total_vcpu']
            all_total_sas_vmem = all_total_sas_vmem + hypernode['total_memory']
            total_sas_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_sas_vdisk = all_total_sas_vdisk + total_sas_disk
            all_total_used_sas_vcpu = all_total_used_sas_vcpu + hypernode['used_vcpu']
            all_total_used_sas_vmem = all_total_used_sas_vmem + hypernode['used_memory']
            all_total_used_sas_vdisk = all_total_used_sas_vdisk + hypernode['virtual_disk']
        elif place_group_ids == 'plg-00000001':
            hyper_ssd.append(host_machine)
            total_real_ssd_cpu = hypernode['total_vcpu']/5
            all_total_real_ssd_cpu = all_total_real_ssd_cpu + total_real_ssd_cpu
            all_total_real_ssd_mem = all_total_real_ssd_mem + hypernode['real_total_memory']
            total_real_ssd_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_real_ssd_disk = all_total_real_ssd_disk + total_real_ssd_disk
            all_total_ssd_vcpu = all_total_ssd_vcpu + hypernode['total_vcpu']
            all_total_ssd_vmem = all_total_ssd_vmem + hypernode['total_memory']
            total_ssd_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_ssd_vdisk = all_total_ssd_vdisk + total_ssd_disk
            all_total_used_ssd_vcpu = all_total_used_ssd_vcpu + hypernode['used_vcpu']
            all_total_used_ssd_vmem = all_total_used_ssd_vmem + hypernode['used_memory']
            all_total_used_ssd_vdisk = all_total_used_ssd_vdisk + hypernode['virtual_disk']
        elif place_group_ids == 'plg-00000002':
            hyper_sata.append(host_machine)
            total_real_sata_cpu = hypernode['total_vcpu']/5
            all_total_real_sata_cpu = all_total_real_sata_cpu + total_real_sata_cpu
            all_total_real_sata_mem = all_total_real_sata_mem + hypernode['real_total_memory']
            total_real_sata_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_real_sata_disk = all_total_real_sata_disk + total_real_sata_disk
            all_total_sata_vcpu = all_total_sata_vcpu + hypernode['total_vcpu']
            all_total_sata_vmem = all_total_sata_vmem + hypernode['total_memory']
            total_sata_disk = hypernode['used_disk'] + hypernode['free_disk']
            all_total_sata_vdisk = all_total_sata_vdisk + total_sata_disk
            all_total_used_sata_vcpu = all_total_used_sata_vcpu + hypernode['used_vcpu']
            all_total_used_sata_vmem = all_total_used_sata_vmem + hypernode['used_memory']
            all_total_used_sata_vdisk = all_total_used_sata_vdisk + hypernode['virtual_disk']
        else:
            hyper_other.append(host_machine)


    lenth_sas = len(hyper_sas)
    lenth_ssd = len(hyper_ssd)
    lenth_sata = len(hyper_sata)
    lenth_other = len(hyper_other)

    print "zone: %s\ntotal: %d, sas: %d, ssd: %d, sata: %d, other: %d" %(zone, total_hyper, lenth_sas, lenth_ssd, lenth_sata, lenth_other)

    sas_result =  cal_data(all_total_real_sas_cpu, all_total_real_sas_mem,all_total_real_sas_disk, all_total_sas_vcpu, all_total_sas_vmem, all_total_sas_vdisk, all_total_used_sas_vcpu, all_total_used_sas_vmem, all_total_used_sas_vdisk)
    ssd_result =  cal_data(all_total_real_ssd_cpu, all_total_real_ssd_mem, all_total_real_ssd_disk, all_total_ssd_vcpu, all_total_ssd_vmem, all_total_ssd_vdisk, all_total_used_ssd_vcpu, all_total_used_ssd_vmem, all_total_used_ssd_vdisk)
    sata_result =  cal_data(all_total_real_sata_cpu, all_total_real_sata_mem, all_total_real_sata_disk, all_total_sata_vcpu, all_total_sata_vmem, all_total_sata_vdisk, all_total_used_sata_vcpu, all_total_used_sata_vmem, all_total_used_sata_vdisk)
    
    ws1 = wb['Sheet1']
    ws2 = wb['Sheet2']
    ws3 = wb['Sheet3']
    insertwb(ws1, sas_result)
    insertwb(ws2, ssd_result)
    insertwb(ws3, sata_result)
    wb.save('result' + '-' +  zone + '-' + dt + '.xlsx')
cmd = 'tar czf result-%s.tgz result-*.xlsx' % dt
rm_cmd = 'rm -rf result-*.xlsx'
os.system(cmd)
os.system(rm_cmd)
