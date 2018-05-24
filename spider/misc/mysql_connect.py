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

class MysqlConnect(object):
    def __init__(self,filename):
        self.__file = filename
        self.__host = self.__getconfig()['host']
        self.__user = self.__getconfig()['user']
        self.__password = self.__getconfig()['password']

    def __getconfig(self):
        with open(self.__file) as f:
            configs = yaml.load(f.read())
        f.close()
        return configs

    def getconfig(self):
        return self.__host

    def change_data(self, basename, sql):
        db = pymysql.connect(self.__host,self.__user,self.__password, basename, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            return 0
        except Exception as e:
            db.rollback()
            return e
        finally:
            cursor.close()
            db.close()

    def select_data(self, basename, sql):
        db = pymysql.connect(self.__host,self.__user,self.__password, basename, use_unicode=True, charset="utf8")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except:
            db.rollback()
        else:
            return cursor.fetchall()
        finally:
            cursor.close()
            db.close()

if __name__ == '__main__':
    a = MysqlConnect('mysql_data.yaml')
    in_sql = "update student set birthday = '1990-09-08' where name = 'hello'"
    sql = 'select * from students'
    b = a.change_data('test',in_sql)
    print(b)
    print(a.select_data('test',sql))
