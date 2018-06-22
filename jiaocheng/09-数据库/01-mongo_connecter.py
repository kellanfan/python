#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 21 Jun 2018 05:36:46 PM CST

# File Name: 01-mongo_connecter.py
# Description:

"""
from pymongo import *
client = MongoClient('mongodb://192.168.10.10:27017')
db = client.py3
coll = db.stu
coll.insert({'name':'aa','sex':True})
coll.update({'name':'bbb'},{'$set':{'sex':False}})
coll.remove({'name':'aa'})
print(coll.find_one({'name':'bbb'}))
