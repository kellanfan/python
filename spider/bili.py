#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 16 Nov 2017 10:23:07 AM CST

# File Name: bili.py
# Description:

"""

import urllib2,time,json
import psycopg2
def getreq(url):
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                            'AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    return req

def getdict(url):
    html = urllib2.urlopen(url).read()
    return html

def insert_data(dic):
    try:
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
        cmd = "insert into bili(v_aid, v_view, v_danmaku, v_favorite, v_reply, v_coin, v_share) values (%d,%d,%d,%d,%d,%d,%d)" %(dic['aid'], dic['view'], dic['danmaku'], dic['favorite'], dic['reply'], dic['coin'], dic['share'])
        cur.execute(cmd)
    except:
        print "exec sql failed..."
    finally:
        conn.commit()

conn = psycopg2.connect(database="bilibili", user="postgres", password="Zhu88jie", host="127.0.0.1", port="5432")
cur = conn.cursor()

urls = ["http://api.bilibili.com/x/web-interface/archive/stat?aid={}".format(i) for i in range(20000,40000)]
for url in urls:
    req = getreq(url)
    time.sleep(0.5)
    tmp = getdict(req)
    data = json.loads(tmp)
    if data['code'] == 0:
        insert_data(data['data'])
cur.close()
conn.close()
