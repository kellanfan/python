#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 15 Apr 2019 12:54:09 PM CST

# File Name: mysql2mongo.py
# Description:

"""
import os
import yaml
import pymysql
from pymongo import MongoClient

def mysql_info(sql):
    '''
        获取mysql数据的生成器
    '''
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
        exit()
    else:
        while True:
            yield dict(zip([x[0] for x in cursor.description],[x for x in cursor.fetchone()]))
    finally:
        cursor.close()
        mysql_conn.close()

def get_config():
    '''
        获取配置文件中的配置信息
    '''
    if os.path.exists('mysql2mongo.yaml'):
        with open('mysql2mongo.yaml') as f:
            return yaml.load(f.read())
    else:
        print("未找到配置文件mysql2mongo.yaml")
        exit()

if __name__ == '__main__':
    #获取配置
    configs = get_config()
    try:
        mysql_host = configs['mysql']['host']
        mysql_database = configs['mysql']['database']
        mysql_user = configs['mysql']['user']
        mysql_pass = configs['mysql']['password']
        mysql_command = configs['mysql']['command']
        mongo_host = configs['mongo']['host']
        mongo_port = configs['mongo']['port']
        mongo_database = configs['mongo']['database']
        mongo_collections = configs['mongo']['collections']
    except:
        print('缺少参数..')
        exit()

    #创建mysql和mongodb的连接
    try:
        mysql_conn = pymysql.connect(mysql_host,mysql_user,mysql_pass,mysql_database,use_unicode=True, charset="utf8")
        cursor = mysql_conn.cursor()
        mongo_conn = MongoClient(mongo_host,mongo_port)
        mongo_db = mongo_conn[mongo_database]
        mycoll = mongo_db[mongo_collections]
    except:
        print("连接数据库失败..")
        exit()

    infos = mysql_info(mysql_command)
    while True:
        try:
            info = next(infos)
            print("insert [%s] to mongodb.."%info['name'])
            mycoll.insert(info)
        except:
            print('Done.')
            break
