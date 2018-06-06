#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import time
from misc import which_is_sunday
from misc import openurl
from misc import mysql_connect

def send_mysql(part, info):
    sql = "insert into runningman(phase, panurl, password) value ('%s', '%s', '%s')"%(part,info[0],info[1])
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data('spiderdata', sql)
    if code == 0:
        print('%s ok'%part)
    else:
        print('%s error'%part)


def main():
    #构建url
    url_head = 'http://www.runningman-fan.com/'
    url_end = '-zz.html'
    week_list = which_is_sunday.sunday(18)

    for part in week_list:
        #构建最终的url
        url = url_head + str(part) + url_end
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
            print(part,html,password)
            info = tuple(html + password)
            if len(info) == 2:
                send_mysql(part, info)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
