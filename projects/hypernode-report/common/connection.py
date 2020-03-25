# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   connection.py
@Time    :   2020/03/17 12:32:57
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import urllib, urllib2, datetime
import json
import base64, hmac
from hashlib import sha256
import sys
sys.path.append('../actions')
from actions.zones import Zones
from actions.plg import Plg
from actions.bots import Describe_Bots
from actions.billing import Billing
class APIConnection(object):
    def __init__(self, api_url, access_key_id, secret_access_key):
        self.api_url = api_url
        self.__access_key_id = access_key_id
        self.__secret_access_key = secret_access_key
        self.__base_para = {
            'version':'1',
            'signature_method':'HmacSHA256',
            'signature_version':'1',
            'access_key_id': self.__access_key_id,
        }
        self.__header = {
            'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/56.0.2924.87 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            }

    def build_request(self, action_data):
        request = {}
        string_to_sign = 'GET\n/iaas/\n'
        pairs = []
        request.update(self.__base_para)
        request.update(action_data)
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        request['time_stamp'] = time
        keys = sorted(request.keys())
        for key in keys:
            val = request[key].encode('utf-8')
            pairs.append(urllib.quote(key, safe='') + '=' +
                         urllib.quote(val, safe='-_~'))
        qs = '&'.join(pairs)
        string_to_sign += qs
        data = urllib.urlencode(request)
        h = hmac.new(self.__secret_access_key, digestmod=sha256)
        h.update(string_to_sign)
        signature = urllib.quote_plus(base64.b64encode(h.digest()).strip())
        return self.api_url + '?' + data + '&signature=' + signature

    def send_request(self, request):
        try:
            req = urllib2.Request(request, headers = self.__header)
            response = urllib2.urlopen(req)
        except Exception as e:
            print("ERROR: API接口无响应，请检查: 1.API地址及端口配置是否正确 2.API服务是否正常")
            print("错误输出信息: {}".format(e))
            sys.exit()
        return json.loads(response.read())

    def describe_zones(self):
        zones_body = Zones()
        request = self.build_request(zones_body())
        return self.send_request(request)

    def describe_place_groups(self,zone):
        plg_body = Plg(zone)
        request = self.build_request(plg_body())
        return self.send_request(request)

    def describe_bots(self, zone, offset='0'):
        bots_body = Describe_Bots(zone, offset)
        request = self.build_request(bots_body())
        return self.send_request(request)

    def get_charge_records(self,zone,start_time,end_time):
        body = Billing(zone,start_time,end_time)
        request = self.build_request(body())
        return self.send_request(request)
