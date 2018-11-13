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

    def open(self,basename):
        #可以把数据库名basename放在实例属性中，既可以当做参数，也可以写到yaml配置文件中,这个无所谓，因为现在所有
        #代码都是用一个yaml文件，暂时就先放在这设置就好。
        self.db = pymysql.connect(self.__host,self.__user,self.__password, basename, use_unicode=True, charset="utf8")
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def change_data(self, basename, sql):
        try:
            self.open(basename)
            self.cursor.execute(sql)
            self.db.commit()
            return 0
        except Exception as e:
            self.db.rollback()
            return e
        finally:
            self.close()

    def select_data(self, basename, sql):
        try:
            self.open(basename)
            self.cursor.execute(sql)
        except Exception as e:
            return e
        else:
            return self.cursor.fetchall()
        finally:
            self.close()

if __name__ == '__main__':
    a = MysqlConnect('mysql_data.yaml')
    sql = input("the sql: ")
    print(len(a.select_data('spiderdata',sql)))
