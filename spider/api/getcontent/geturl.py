#!/usr/bin/python

import urllib2, urllib, json, datetime
import base64, hmac
from hashlib import sha256
from key import value

def geturl(data, zone, access_key_id, secret_access_key):
    url = 'http://api.taikangcloud.com:8882/iaas/'
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    data['time_stamp'] = time
    data['access_key_id'] = access_key_id
    data['zone'] = zone
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
    h = hmac.new(secret_access_key, digestmod=sha256)
    h.update(string_to_sign)
    sign = base64.b64encode(h.digest()).strip()
    signature = urllib.quote_plus(sign)
    url2 = url + '?' + data + '&signature=' + signature
    return url2
