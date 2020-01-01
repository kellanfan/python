# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   pg_client.py
@Time    :   2019/11/03 18:13:37
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import json
import etcd
import psycopg2
#from log.logger import logger

class Mypostgres(object):
    def __init__(self):
        etc_client = etcd.Client(host='192.168.1.2', port=2379)
        etc_result = etc_client.read('/python/info/postgresql')
        postgresql_info = json.loads(etc_result.value)
        self.db=psycopg2.connect(database=postgresql_info['database'], user=postgresql_info['user'], password=postgresql_info['password'], host=postgresql_info['host'], port=postgresql_info['port'])
        self.cursor=self.db.cursor()

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
            #logger.error(e)
            return e

    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            #logger.error(e)
            return e
        else:
            return self.cursor.fetchall()
if __name__ == "__main__":
    postgresql = Mypostgres()
    select_cmd = 'select public_time from dian_ying_tian_tang order by public_time desc limit 1'
    last_time = postgresql.select_data(select_cmd)[0][0].strip()
    print(last_time)