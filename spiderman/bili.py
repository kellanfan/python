# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   bili.py
@Time    :   2019/05/27 09:55:54
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import platform
import time
import os
import json
from misc import mysql_connect
from misc import openurl

def insert_data(dic):
    if  dic['view'] == '--':
        dic['view'] = 0
    elif dic['danmaku'] == '--':
        dic['danmaku'] = 0
    elif dic['favorite'] == '--':
        dic['favorite'] = 0
    elif dic['reply'] == '--':
        dic['reply'] = 0
    elif dic['coin'] == '---':
        dic['coin'] = 0
    elif dic['share'] == '--':
        dic['share'] = 0
    cmd = "insert into bili(v_aid, v_view, v_danmaku, v_favorite, v_reply, v_coin, v_share) values (%d,%d,%d,%d,%d,%d,%d)"%(dic['aid'], dic['view'], dic['danmaku'], dic['favorite'], dic['reply'], dic['coin'], dic['share'])
    code = mysql_conn.change_data(cmd)
    if code == 0:
        print('[%d] ok'%dic['aid'])
    else:
        print('[%d] error,message: [%s]'%(dic['aid'], code))

if __name__ == "__main__":
    if 'Windows' in platform.platform():
        mysql_conn = mysql_connect.MysqlConnect(os.path.join(os.path.abspath(os.path.curdir),'python\\spider\\misc\\mysql_data.yaml'))
    elif 'Linux' in platform.platform():
        mysql_conn = mysql_connect.MysqlConnect(os.path.join(os.path.abspath(os.path.curdir),'misc/mysql_data.yaml'))
    else:
        pass
    urls = ["http://api.bilibili.com/x/web-interface/archive/stat?aid={}".format(i) for i in range(20000,40000)]
    for url in urls:
        ourl = openurl.OpenUrl(url)
        code,doc = ourl.openurl()
        time.sleep(0.5)
        if code == 200:
            data = json.loads(doc)
            if data['code'] == 0: 
                insert_data(data['data'])
