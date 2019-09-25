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

from lxml import etree
from misc.openurl import OpenUrl

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
        except:
            return None

if __name__ == "__main__":
    start_url='https://www.dytt8.net/'
    ourl = OpenUrl(start_url)
    code,html = ourl.openurl()
    if code == 200:
        info_list = []
        movie_list = getMovieUrl(html)
        for url in movie_list:
            tmp = getMovieInfo(url)
            if tmp:
                info_list.append(tmp)
        print(info_list)
