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
from bs4 import BeautifulSoup 
from misc.openurl import OpenUrl
from log.create_logger import create_logger

logger = create_logger()
base_url = 'http://wufazhuce.com/article/'

mongo_client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = mongo_client["spider"]
coll = db["one"]
cur_last_id = list(coll.find().sort('article_id'))[-1]['article_id']

fail_time = 0

while True:
    cur_last_id += 1
    data = {}
    ourl = OpenUrl(base_url + str(cur_last_id))
    code,doc = ourl.run()
    if code == 200:
        soup = BeautifulSoup(doc, 'lxml')
        data['article_id'] = cur_last_id
        data["title"] = soup.find('h2',class_='articulo-titulo').text.strip()
        data["autor"] = soup.find('p',class_='articulo-autor').text.strip()
        data["content"] = soup.find('div',class_='articulo-contenido').text.strip()
        
        try:
            coll.insert_one(data)
            logger.info("insert [{}] successful".format(data["title"]))
        except Exception as e:
            logger.error("insert [{0}] failed: [{1}]".format(data["title"],e))
            continue
        time.sleep(1)
    else:
        fail_time += 1
        logger.error("Get [{}] failed".format(cur_last_id))
        if fail_time > 20:
            logger.critical("Too many Fail times, break!")
            break