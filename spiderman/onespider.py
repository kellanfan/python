# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   onespider.py
@Time    :   2020/04/10 09:23:10
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import pymongo
import time
from lxml import etree
from misc.openurl import OpenUrl
from log.create_logger import create_logger
#logger = create_logger()

base_url = 'http://wufazhuce.com/article/'

title_reg = '//h2[@class="articulo-titulo"]/text()'
autor_reg = '//p[@class="articulo-autor"]/text()'
content_reg = '//div[@class="articulo-contenido"]/child::text()'

mongo_client = pymongo.MongoClient("mongodb://192.168.1.2:27017/")
db = mongo_client["spider"]
coll = db["one"]

for num in range(275,5000):
    ourl = OpenUrl(base_url + str(num))
    code,doc = ourl.run()
    data = {}
    if code == 200:
        selecter = etree.HTML(doc)
        title = selecter.xpath(title_reg)[0]
        autor = selecter.xpath(autor_reg)[0]
        content = '\n'.join(selecter.xpath(content_reg))
        if content.strip():
            data["content"] = content.strip()
        else:
            print("[{}] has no content".format(title.strip()))
            continue
        data['article_id'] = num
        data["title"] = title.strip()
        data["autor"] = autor.strip()
        
        try:
            coll.insert_one(data)
            print("insert [{}] successful".format(title.strip()))
        except Exception as e:
            print("insert [{0}] failed: [{1}]".format(title.strip(),e))
            continue
        time.sleep(1)
    else:
        print("Get [{}] failed".format(num))