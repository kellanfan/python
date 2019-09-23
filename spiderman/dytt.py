# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   dytt.py
@Time    :   2019/07/09 17:05:57
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
from misc import openurl
from lxml import etree

url = 'https://www.dytt8.net/'
ourl = openurl.OpenUrl(url,'gb2312')
code,doc = ourl.openurl()
if code == 200:
    selector = etree.HTML(doc)
    url_list = selector.xpath('//a/@href')
    for urls in url_list:
        if urls.startswith('/html'):
            print(urls)