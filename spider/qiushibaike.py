#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 25 Nov 2018 07:50:36 PM CST

# File Name: qiushibaike.py
# Description:

"""
import json
import re
from lxml import etree
from misc import openurl

def main():
    url = 'https://www.qiushibaike.com/8hr/page/1/'
    ourl = openurl.OpenUrl(url)
    code, doc = ourl.openurl()
    if code == 200:
        selector = etree.HTML(doc)
        content = selector.xpath("//div[contains(@id,'qiushi_tag')]")
        item = []
        for site in content:
            result = {}
            try:
                imgUrl = site.xpath('./div/a/img/@src')[0]
                username = site.xpath('./div/a/img/@alt')[0]
                content = site.xpath('.//div[@class="content"]/span/text()')[0].strip()
                vote = site.xpath('.//i/text()')[0]
                comment = site.xpath('.//i/text()')[1]
            except:
                print("something failed..")
                continue

            result['imgUrl'] = imgUrl
            result['username'] = username
            result['content'] = content
            result['vote'] = vote
            result['comment'] = comment
            
            item.append(result)
    
    with open('qiubai.json', 'w+') as f:
        f.write(json.dumps(item, ensure_ascii=False))

if __name__ == '__main__':
    main()
