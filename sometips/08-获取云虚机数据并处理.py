# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   08-获取云虚机数据并处理.py
@Time    :   2019/05/21 11:27:02
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

from qingcloud.iaas import APIConnection
from pathlib import Path
import platform
import yaml
import datetime

def handledata(ret):
    """
        处理获取到的数据
    """
    cpu_maxvalue = None
    cpu_avgvalue = None
    mem_maxvalue = None
    mem_avgvalue = None
    disk_read_maxvalue = None
    disk_read_avgvalue = None
    disk_write_maxvalue = None
    disk_write_avgvalue = None
    if 'meter_set' in ret.keys():
        for items in ret['meter_set']:
            if not items['data']:
                continue
            data_list = [x[1] if isinstance(x,list) else x for x in items['data']]
            if items['meter_id'] == 'cpu':
                try:
                    cpu_maxvalue = max(data_list)/10
                    cpu_avgvalue = '{:.2f}'.format(sum(data_list)/len(data_list)/10)
                except:
                    pass
            elif items['meter_id'] == 'memory':
                try:
                    mem_maxvalue = max(data_list)/10
                    mem_avgvalue = '{:.2f}'.format(sum(data_list)/len(data_list)/10)
                except:
                    pass

            elif items['meter_id'] == 'disk-iops-os':
                data_list = [x[1] if isinstance(x[1],list) else x for x in items['data']]
                try:
                    disk_read = [x[0] for x in data_list]
                    disk_read_maxvalue = max(disk_read)
                    disk_read_avgvalue = '{:.2f}'.format(sum(disk_read)/len(disk_read))
                    disk_write_org = [x[1] for x in data_list]
                    disk_write = [x[1] if isinstance(x,list) else x for x in disk_write_org]
                    disk_write_maxvalue = max(disk_write)
                    disk_write_avgvalue = '{:.2f}'.format(sum(disk_write)/len(disk_write))
                except:
                    pass
            else:
                pass
    return (cpu_maxvalue, cpu_avgvalue,
            mem_maxvalue, mem_avgvalue,
            disk_read_maxvalue, disk_read_avgvalue,
            disk_write_maxvalue, disk_write_avgvalue)
if __name__ == "__main__":
    if platform.system() == 'Windows':
        curdir = Path.cwd() / 'python/sometips'
    elif platform.system() == 'Linux':
        curdir = Path.cwd()

    with open(curdir/'qingcloud.yaml') as f:
        configs = yaml.load(f.read())

    zone = configs.get('zone')
    access_key_id = configs.get('access_key_id')
    secret_access_key = configs.get('secret_access_key')
    host = configs.get('host')

    #conn = APIConnection(access_key_id, secret_access_key, zone,  host=host, port='7777', protocol='http')
    conn = APIConnection(access_key_id, secret_access_key, zone, host=host)
    nowtime = datetime.datetime.now()
    start_one_time = (nowtime + datetime.timedelta(days=-1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    start_sev_time = (nowtime + datetime.timedelta(days=-7)).strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = nowtime.strftime('%Y-%m-%dT%H:%M:%SZ')
    with open(curdir/'instance_list.txt') as f:
        for line in g.readlines():
            instance_id = line.strip()
            one_day_ret = conn.get_monitoring_data(instance_id ,['cpu','memory','disk-iops-os'],'5m', start_one_time, end_time)
            sev_day_ret = conn.get_monitoring_data(instance_id ,['cpu','memory','disk-iops-os'],'5m', start_sev_time, end_time)
            one_day_result_list = handledata(one_day_ret)
            sev_day_result_list = handledata(sev_day_ret)
            print('''instance_id: {}
    one_day_info:
         cpu_maxvalue: {}
         cpu_avgvalue: {}
         mem_maxvalue: {}
         mem_avgvalue: {}
         disk_read_maxvalue: {}
         disk_read_avgvalue: {}
         disk_write_maxvalue: {}
         disk_write_avgvalue: {}\n'''.format(
         instance_id,one_day_result_list[0],one_day_result_list[1],
         one_day_result_list[2],one_day_result_list[3],
         one_day_result_list[4],one_day_result_list[5],
         one_day_result_list[6],one_day_result_list[7]))
            print('''
    sev_day_info:
         cpu_maxvalue: {}
         cpu_avgvalue: {}
         mem_maxvalue: {}
         mem_avgvalue: {}
         disk_read_maxvalue: {}
         disk_read_avgvalue: {}
         disk_write_maxvalue: {}
         disk_write_avgvalue: {}\n'''.format(
         sev_day_result_list[0],sev_day_result_list[1],
         sev_day_result_list[2],sev_day_result_list[3],
         sev_day_result_list[4],sev_day_result_list[5],
         sev_day_result_list[6],sev_day_result_list[7]))