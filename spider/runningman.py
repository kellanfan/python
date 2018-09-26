#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os,sys
import time
from misc import which_is_sunday
from misc import openurl
from misc import mysql_connect
from misc.logger import Logger

class RM(object):
    def __init__(self, year):
        mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
        self.logger = mylog.outputLog()
        self.year = year
        self.week_list = which_is_sunday.sunday(year)

    def send_mysql(self, part, info):
        sql = "insert into runningman(phase, panurl, password) value ('%s', '%s', '%s')"%(part,info[0],info[1])
        connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
        code = connect.change_data('spiderdata', sql)
        if code == 0:
            self.logger.info('%s ok'%part)
        else:
            self.logger.error('%s error,message: %s'%(part,code))


    def run(self):
        #构建url
        url_head = 'http://www.runningman-fan.com/'
        for part in self.week_list:
            #构建最终的url
            if self.year < 17:
                url = url_head + str(part) + '.html'
            else:
                url = url_head + str(part) + '-zz.html'
            #正则匹配
            html_reg = re.compile(r'<a href="(.+://pan.baidu.com/s/\w*)')
            pass_reg = re.compile(r'[密码|度盘][：|:][ ]?(\w{4})?')
            #获取数据
            ourl = openurl.OpenUrl(url)
            code,html = ourl.openurl()

            if code == 200:
                password = list(set(re.findall(pass_reg, html)))
                for pw in password:
                    if pw != 'body' and pw != '':
                        password = [pw]
                html = re.findall(html_reg, html)
                info = tuple(html + password)
                if len(info) == 2:
                    self.send_mysql(part, info)
            time.sleep(0.5)

def select_mysql(year):
    sql = "select phase from runningman where phase like '%s%%' order by phase desc limit 1" %year
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    return connect.select_data('spiderdata', sql)

if __name__ == '__main__':
    year = input("请输入年份：")
    code = select_mysql(year)
    if code:
        if year in code[0][0]:
            print('data had it...')
            sys.exit()
    else:
        a = RM(int(year))
        a.run()
