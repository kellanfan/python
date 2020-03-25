#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Wed 25 Mar 2020 07:33:49 PM CST

# File Name: a.py
# Description:

"""
import re
import sys
import datetime
import yaml
from common.connection import APIConnection

def gen_time(dt):
    dt = map(lambda x: int(x),re.split('-| |:', dt))
    return datetime.datetime(int(dt[0]),int(dt[1]),int(dt[2]),int(dt[3]),int(dt[4]),int(dt[5]),).strftime('%Y-%m-%dT%H:%M:%SZ')

def main():
    try:
        with open('./config.yaml') as f:
            config = yaml.load(f.read())
        url = config['url']
        access_key_id = config['access_key_id']
        secret_access_key = config['secret_access_key']
    except Exception as e:
        print("ERROR: 加载配置文件失败！请检查配置文件！")
        print("错误输出信息: {}".format(e))
        sys.exit()
    start_time = gen_time('2020-02-01 00:00:00')
    end_time = gen_time('2020-02-29 00:00:00')
    conn = APIConnection(url, access_key_id, secret_access_key)
    rep = conn.get_charge_records('pek3a',start_time,end_time)
    for item in rep['charge_record_set']:
        print(item['resource_id'],item['resource_type'],item['fee'])

if __name__ == '__main__':
    main()
