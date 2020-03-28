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
import sys
sys.path.append('..')
from log.create_logger import create_logger
logger = create_logger('pg_client')

class Mypostgres(object):
    def __init__(self):
        try:
            etc_client = etcd.Client(host='192.168.1.2', port=2379)
            etc_result = etc_client.read('/python/info/postgresql')
            self.postgresql_info = json.loads(etc_result.value)
        except Exception as e:
            self.postgresql_info = {}
            logger.error('Connect to Etcd server failed: [{}]'.format(e))

    def __init_conn(self):
        try:
            conn=psycopg2.connect(
                database=self.postgresql_info['database'],
                user=self.postgresql_info['user'],
                password=self.postgresql_info['password'],
                host=self.postgresql_info['host'],
                port=self.postgresql_info['port']
            )
        except Exception as e:
            conn = None
            logger.error('Connect to PostgreSQL failed: [{0}]'.format(e))
        return conn

    def execute(self, sql, parameters=None):
        '''
        @param sql - the sql statement to be executed.
            e.g. "INSERT INTO test (num, data) VALUES (%s, %s)"
        @param parameters - a sequence of variables in the sql operation.
            e.g. (100, "abc") or [10, 'def']
        '''
        action = sql.split()[0].strip().lower()
        if action not in ['select', 'insert', 'delete', 'update', 'create']:
            logger.error('The action [{0}] of SQL [{1}] is not supported!'.format(action, sql))
            return None

        conn = self.__init_conn()
        if conn is not None:
            cursor = conn.cursor()
        else:
            return None

        try:
            cursor.execute(sql, parameters)
            if action == 'select':
                rows = cursor.fetchall()
                result = rows
            else:
                conn.commit()
                rowcount = cursor.rowcount
                result = rowcount
        except Exception as e:
            conn.rollback()
            result = None
            logger.error('Execute SQL [{0}] failed: [{1}]'.format(sql, e))
        finally:
            cursor.close()
            conn.close()

        return result

if __name__ == "__main__":
    postgresql = Mypostgres()
    select_cmd = 'select public_time from dian_ying_tian_tang order by public_time desc limit 1'
    insert_sql = "insert into bili(v_aid, v_view, v_danmaku, v_favorite, v_reply, v_coin, v_share) values (%s,%s,%s,%s,%s,%s,%s)"
    parameters = [20000,14711,90,209,171,21,11]
    last_time = postgresql.execute(select_cmd)[0][0].strip()
    count = postgresql.execute(insert_sql, parameters=parameters)
    print(last_time)
    print(count)