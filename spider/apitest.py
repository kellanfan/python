#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 08 Jun 2017 09:06:25 AM CST

# File Name: apitest.py
# Description:

"""
import urllib2, urllib, json, datetime
import base64, hmac
from hashlib import sha256
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
secret_access_key = 'zUD7r8f1X8R28MHgKNOWUCm0NWD0WucyZv1H8aAg'
url = 'https://api.qingcloud.com/iaas/'
data={'access_key_id':'JKEDNDMVPAFWGXFTEAXL',
      'action':'DescribeInstances',
      'version':'1',
      'signature_method':'HmacSHA256',
      'signature_version':'1',
      'time_stamp':time,
      'zone':'pek3a'
}
keys = sorted(data.keys())
string_to_sign = 'GET\n/iaas/\n'
pairs = []
for key in keys:
    val = data[key].encode('utf-8')
    pairs.append(urllib.quote(key, safe='') + '=' +
                urllib.quote(val, safe='-_~'))
qs = '&'.join(pairs)
string_to_sign += qs
data = urllib.urlencode(data)
h = hmac.new(secret_access_key,digestmod=sha256)
h.update(string_to_sign)
sign = base64.b64encode(h.digest()).strip()
signature = urllib.quote_plus(sign)
url2 = url + '?' + data + '&signature=' + signature
response = urllib2.urlopen(url2)
apicontent = response.read()
print apicontent

