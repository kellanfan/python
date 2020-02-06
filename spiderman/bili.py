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
import json
import time
from misc.pg_client import Mypostgres
from misc.openurl import OpenUrl

def insert_data(dic):
    if dic['view'] == '--':
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
    else:
        pass
    sql = '''insert into bili(
            v_aid, v_view, v_danmaku, v_favorite, v_reply, v_coin, v_share) 
            values (%s,%s,%s,%s,%s,%s,%s)
        '''%(dic['aid'], dic['view'], dic['danmaku'], dic['favorite'], dic['reply'], dic['coin'], dic['share'])
    count = pg_conn.execute(sql)
    if count:
        print('[{}] ok'.format(dic['aid']))
    else:
        print('[{0}] error,message: [{1}]'.format(dic['aid'], count))

if __name__ == "__main__":
    pg_conn = Mypostgres()
    urls = ["http://api.bilibili.com/x/web-interface/archive/stat?aid={}".format(i) for i in range(20000,40000)]
    for url in urls:
        ourl = OpenUrl(url)
        code,doc = ourl.run()
        time.sleep(0.5)
        if code == 200:
            data = json.loads(doc)
            if data['code'] == 0: 
                insert_data(data['data'])