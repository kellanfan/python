# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   电影天堂.py
@Time    :   2019/09/24 14:28:54
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   获取电影天堂的最新电影资源
'''

# here put the import lib
import json
import etcd
import psycopg2
from lxml import etree
from misc.openurl import OpenUrl
class Mypostgres(object):
    def __init__(self):
        etc_client = etcd.Client(host='10.91.158.2', port=2379)
        etc_result = etc_client.read('/project/spiderman/postgres')
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
            return e

    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            return e
        else:
            return self.cursor.fetchall()

def getMovieUrl(html):
    selecter = etree.HTML(html)
    movie_url = selecter.xpath("//div[@class='bd3']/div[@class='bd3r'][1]/div/div[@class='bd3rl']/div[@class='co_area2'][1]//a/@href")
    movie_url = set(movie_url)
    movie_url.remove('/app.html')
    movie_url.remove('/html/gndy/dyzz/index.html')    
    return movie_url

def getMovieInfo(url):
    full_url = 'https://www.dytt8.net/' + url
    ourl = OpenUrl(full_url,'gb2312')
    code,html = ourl.openurl()
    info = {}
    if code==200:
        selecter = etree.HTML(html)
        try:
            info['name'] = selecter.xpath("//div[@class='title_all']/h1/font/text()")[0]
            info['public_time'] = selecter.xpath("//div[@class='co_content8']/ul/text()")[0].strip().split('：')[1]
            info['downlink'] = selecter.xpath("//tbody/tr/td/a/text()")[0]
            return info
        except Exception as e:
            raise e
    else:
        return html

if __name__ == "__main__":
    start_url='https://www.dytt8.net/'
    ourl = OpenUrl(start_url)
    code,html = ourl.openurl()
    info_list = []
    if code == 200:
        movie_list = getMovieUrl(html)
        for url in movie_list:
            tmp = getMovieInfo(url)
            if tmp:
                info_list.append(tmp)
    else:
        print(html)
        exit()
    postgresql = Mypostgres()
    select_cmd = 'select public_time from dian_ying_tian_tang order by public_time desc limit 1'
    last_time = postgresql.select_data(select_cmd)[0][0].strip()
    for info in info_list:
        if info['public_time'] > last_time:
            cmd = "insert into dian_ying_tian_tang(name,public_time,downlink) values ('%s', '%s', '%s')"%(info['name'],info['public_time'],info['downlink'])
            res = postgresql.change_data(cmd)
            if res == 0:
                print("insert [%s] ok.."%info['name'])
            else:
                print(res)
    postgresql.close()