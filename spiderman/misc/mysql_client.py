#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 23 May 2018 08:15:18 PM CST

# File Name: mysql_connect.py
# Description: 关于编码问题可看: https://stackoverflow.com/questions/3942888/unicodeencodeerror-latin-1-codec-cant-encode-character

"""
import etcd
import pymysql
import json
from misc.logger import logger


class MysqlConnect(object):
    def __init__(self):
        etc_client = etcd.Client(host='etcd', port=2379)
        etc_result = etc_client.read('/project/spiderman/mysql')
        mysql_info = json.loads(etc_result.value)
        self.db = pymysql.connect(mysql_info['host'],mysql_info['user'],mysql_info['password'], mysql_info['database'], use_unicode=True, charset="utf8")
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def change_data(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return 0
        except Exception as e:
            self.db.rollback()
            logger.error(e)
            return e
        finally:
            self.close()

    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            logger.error(e)
            return e
        else:
            return self.cursor.fetchall()
        finally:
            self.close()

if __name__ == '__main__':
    a = MysqlConnect()
    sql = input("the sql: ")
    print(a.select_data(sql))
