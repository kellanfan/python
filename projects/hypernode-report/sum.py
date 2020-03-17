# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   sum.py
@Time    :   2020/03/17 13:09:36
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import yaml
from common.connection import APIConnection
from common.resource import HyperData

def check_status(content_botset):
    error_status_hyper = []
    error_info_hyper = []
    for hypernode in content_botset:
        status = hypernode['status']
        if status not in ['active', 'standby']:
            error_status_hyper.append(hypernode['host_machine'].encode('utf-8'))
        elif not hypernode.has_key('real_total_memory'):
            error_info_hyper.append(hypernode['host_machine'].encode('utf-8'))
    print("="*50)
    print("下列节点未纳入统计:")
    print("\033[0;31m  状态异常节点:\033[0m {}".format(error_status_hyper))
    print("\033[0;31m  获取信息异常节点:\033[0m {}".format(error_info_hyper))
    print("="*50)

def main():
    plg_map = {}
    try:
        with open('./config.yaml') as f:
            config = yaml.load(f.read())
    except Exception as e:
        print("Load config file Failed: [{}]".format(e))
    else:
        url = config.get('url')
        access_key_id = config.get('access_key_id')
        secret_access_key = config.get('secret_access_key')

    conn = APIConnection(url, access_key_id, secret_access_key)
    zones_info = conn.describe_zones()
    for zone_info in zones_info['zone_set']:
        zone = zone_info['zone_id']
        print("{}:".format(zone))
        
        plgs_info = conn.describe_place_groups(zone)
        plg_list = [plg_info['place_group_id'].encode('utf-8') for plg_info in plgs_info['place_group_set']]
        
        content = conn.describe_bots(zone)
        total_hyper = content['total_count']
        offset = 100
        content_botset1 = []
        while True:
            if total_hyper > offset:
                content1 = conn.describe_bots(zone, str(offset))
                content_botset1 += content1['bot_set']
                offset += 100
            else:
                break
        if content_botset1:
            content_botset = content_botset1 + content['bot_set']
        else:
            content_botset = content['bot_set']
        
        check_status(content_botset)

        for plg in plg_list:
            plg_info = HyperData(content_botset, plg)
            count,infomations = plg_info.cal_data()
            if count != 0:
                print(
'''{0}: 
    数量: {1}
    统计信息：
        物理总cpu数: {2}\t物理总内存: {3}\t物理总磁盘容量: {4}
        物理CPU使用率: {5}\t物理内存使用率: {6}\t物理磁盘使用率: {7}
        虚拟总vcpu数: {8}\t虚拟总内存数: {9}\t虚拟总磁盘数: {10}
        虚拟使用CPU数: {11}\t虚拟使用内存数: {12}\t虚拟使用磁盘数: {13}
        虚拟剩余CPU数: {14}\t虚拟剩余内存数: {15}\t虚拟剩余磁盘数: {16}
        虚拟cpu使用率: {17}\t虚拟内存使用率: {18}\t虚拟磁盘使用率: {19}'''.format(plg, count,
        infomations[0],infomations[1],infomations[2],
        infomations[3],infomations[4],infomations[5],
        infomations[6],infomations[7],infomations[8],
        infomations[9],infomations[10],infomations[11],
        infomations[12],infomations[13],infomations[14],
        infomations[15],infomations[16],infomations[17]))
            else:
                continue

if __name__ == "__main__":
    main()