#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 19 Aug 2018 10:16:03 PM CST

# File Name: hypernode.py
# Description:

"""
import urllib, urllib2, datetime
import json
import base64, hmac
from hashlib import sha256
from key import value

class Describe_Bots(object):
    def __init__(self, zone, url, offset='0'):
        self.__secret_access_key = value.get('secret_access_key')
        self.__url = url
        self.__data = { 
            'action':'DescribeBots',
            'version':'1',
            'limit':'100',
            'offset': offset,
            'signature_method':'HmacSHA256',
            'signature_version':'1',
            'zone': zone,
            'access_key_id': value.get('access_key_id'),
            }
        self.__header = {
            'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/56.0.2924.87 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }
    def __geturl(self):
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.__data['time_stamp'] = time
        keys = sorted(self.__data.keys())
        string_to_sign = 'GET\n/iaas/\n'
        pairs = []
        for key in keys:
            val = self.__data[key].encode('utf-8')
            pairs.append(urllib.quote(key, safe='') + '=' +
                         urllib.quote(val, safe='-_~'))
        qs = '&'.join(pairs)
        string_to_sign += qs
        data = urllib.urlencode(self.__data)
        h = hmac.new(self.__secret_access_key, digestmod=sha256)
        h.update(string_to_sign)
        sign = base64.b64encode(h.digest()).strip()
        signature = urllib.quote_plus(sign)
        url2 = self.__url + '?' + data + '&signature=' + signature
        return url2

    def run(self):
        url = self.__geturl()
        req = urllib2.Request(url, headers = self.__header)
        response = urllib2.urlopen(req)
        return json.loads(response.read())

if __name__ == '__main__':
    a = Describe_Bots('zone_id','http://api.test.com')
    print a.run()
