#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 23 May 2018 08:15:18 PM CST

# File Name: mysql_connect.py
# Description: 关于编码问题可看: https://stackoverflow.com/questions/3942888/unicodeencodeerror-latin-1-codec-cant-encode-character

"""
import pymysql
import yaml
import sys
#本地logger模块
#from logger import Logger

class MysqlConnect(object):
    def __init__(self,filename):
        self.__file = filename
        self.__configs = self.__getconfig()
        #self.__mylogger = Logger('mysql_log.yaml').outputLog()
        try:
            self.__host = self.__configs['host']
            self.__user = self.__configs['user']
            self.__password = self.__configs['password']
            self.__database = self.__configs['database']
        except:
            #self.__mylogger.error('配置文件中缺少相关参数，请检查..')
            sys.exit()

    def __getconfig(self):
        with open(self.__file) as f:
            configs = yaml.load(f.read())
        return configs

    def open(self):
        self.db = pymysql.connect(self.__host,self.__user,self.__password, self.__database, use_unicode=True, charset="utf8")
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def change_data(self, sql):
        try:
            self.open()
            self.cursor.execute(sql)
            self.db.commit()
            return 0
        except Exception as e:
            self.db.rollback()
            #self.__mylogger(e)
            return e
        finally:
            self.close()

    def select_data(self, sql):
        try:
            self.open()
            self.cursor.execute(sql)
        except Exception as e:
            #self.__mylogger(e)
            return e
        else:
            return self.cursor.fetchall()
        finally:
            self.close()

if __name__ == '__main__':
    a = MysqlConnect('mysql_data.yaml')
    sql = input("the sql: ")
    print(a.select_data(sql))
