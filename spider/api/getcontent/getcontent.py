#!/usr/bin/python
'''
use DescribeBots api to get hyper infomations
'''
import urllib2, json
from geturl import geturl
from key import value
import openpyxl, string, time
header = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/56.0.2924.87 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
secret_access_key = value.get('secret_access_key')
access_key_id = value.get('access_key_id')
def Describe_Bots(zone,offset):
    data = { 
         'action':'DescribeBots',
         'version':'1',
         'limit':'100',
         'offset':offset,
         'signature_method':'HmacSHA256',
         'signature_version':'1',
    }

    url = geturl(data, zone, access_key_id, secret_access_key)
    req = urllib2.Request(url, headers = header)
    response = urllib2.urlopen(req)
    page = response.read()
    content = json.loads(page)
    return content
