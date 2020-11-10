# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   20-harbor-sdk.py
@Time    :   2020/11/09 18:17:00
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   curl版本的sdk
'''

# here put the import lib
import requests
import subprocess
import json
import sys

def exec_cmd(command):
    ret = subprocess.run(command,shell=True,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE,
        encoding="utf-8",timeout=5)
    return {'ret': ret.returncode, 'out': ret.stdout.strip(), 'err': ret.stderr.strip()}
    

class HarborAPI(object):
    def __init__(self, url, username, passwd, version, protocol="https"):
        '''
        init the request
        '''
        if version.startswith('v1'):
            self.api_url = 'api'
            self.version = 'v1'
        elif version.startswith('v2'):
            self.api_url = 'api/v2.0'
            self.version = 'v2'
        else:
            print("ERROR: Can not support the version: [{}]".format(version))
            sys.exit(1)
        self.header = 'Content-Type: application/json'
        self.par_cmd = 'curl -u "{0}:{1}" -H "{2}" '.format(
                    username, passwd, self.header)
        self.head_url = '{0}://{1}/{2}'.format(protocol, url, self.api_url)

    def __base_ret(self, key, method):
        ret = exec_cmd('{0} -i -X {1} "{2}/{3}"'.format(
                    self.par_cmd, method, self.head_url, key))
        returncode = ret.get('out').split('\n')[0].split(' ')[1]
        if int(returncode) == 200:
            return ret.get('out').split('\n')[-1]
        else:
            print('Exec Failed: Code is [{}]'.format(returncode))
            return None
    
    def systeminfo(self):
        return self.__base_ret('systeminfo', 'GET')

    def projects(self):
        return self.__base_ret('projects', 'GET')

    def logs(self):
        if self.version == 'v1':
            uri = 'logs'
        elif self.version == 'v2':
            uri = 'audit-logs'
        else:
            pass
        page = 1
        while True:
            ret = self.__base_ret('{0}?page={1}&page_size=100'.format(uri,page), 'GET')
            if ret is not None:
                return ret
            else:
                break
    
if __name__ == '__main__':
    a = HarborAPI('hub.kellan.com', 'admin', 'Harbor12345', 'v2.1.0', 'http')
    ret = a.logs()
    print(ret)