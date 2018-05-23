#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 05 Jul 2017 02:59:09 PM CST

# File Name: test.py
# Description:

"""
import urllib2, json
from geturl import geturl
from key import value

secret_access_key = value.get('secret_access_key')
access_key_id = value.get('access_key_id')
zone = 'pek3a'
data={'action':'DescribeInstances',
      'version':'1',
      'signature_method':'HmacSHA256',
      'signature_version':'1',
      'status': 'running'
     }
url =  geturl(data, zone, access_key_id, secret_access_key)
response = urllib2.urlopen(url)
apicontent = response.read()
content = json.loads(apicontent)
print content
