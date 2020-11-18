# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   20-harbor-sdk.py
@Time    :   2020/11/09 18:17:00
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   
'''

# here put the import lib
import requests
import json
import sys
    
class HarborAPI(object):
    def __init__(self, url, username, passwd, version, protocol="https"):
        '''
        init the request
        '''
        if version.startswith('v1'):
            self.api_url = '{0}://{1}/api/'.format(protocol, url)
            self.version = 'v1'
        elif version.startswith('v2'):
            self.api_url = '{0}://{1}/api/v2.0/'.format(protocol, url)
            self.version = 'v2'
        else:
            print("ERROR: Can not support the version: [{}]".format(version))
            sys.exit(1)
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Content-Type': 'application/json'
        }
        self.auth = (username, passwd)
        self.ret_map = {}
        
    def __get_request(self, key, data=None):
        if data is None:
            ret = requests.get(self.api_url + key, headers=self.headers, auth=self.auth)
        else:
            ret = json.loads(requests.get(self.api_url + key, 
                            headers=self.headers,
                            params=data, 
                            auth=self.auth))
        if ret.status_code == 200:
            return ret.text
        else:
            print('ERRPR: GET request [{0}] Failed: [{1}]'.format(key, ret.status_code))
            return None
    
    def __post_request(self, key, data):
        ret = requests.post(self.api_url + key, data = data, headers=self.headers, auth=self.auth)
        if ret.status_code == 201:
            return True
        else:
            print('ERRPR: POST request [{0}] Failed: [{1}]'.format(key, ret.status_code))
            return False

    def __delete_request(self, key):
        ret = requests.delete(self.api_url + key, headers=self.headers, auth=self.auth)
        if ret.status_code == 200:
            return True
        else:
            print('ERRPR: DELETE request [{0}] Failed: [{1}]'.format(key, ret.status_code))
            return False

    def create_project(self, project_name, is_public = 'false', storage_limit = -1):
        if self.project_info(project_name):
            print('ERROR: project [{}] has exists!'.format(project_name))
            sys.exit(1)
            
        if isinstance(storage_limit, int):
            if storage_limit == -1:
                byte_storage_limit = storage_limit
            elif storage_limit > 0:
                byte_storage_limit = storage_limit * 1024 * 1024 * 1024
            else:
                print('ERROR: The storage limit is invaild: [{}]'.format(storage_limit))
                sys.exit(1)
        else:
            print('ERROR: The storgae limit must be integer values!')
            return None

        data = {
            "project_name": project_name,
            "storage_limit": byte_storage_limit,
            "metadata": {
                "public": is_public
            }
        }
        if self.__post_request('projects', json.dumps(data)):
            return self.project_info(project_name)
        else:
            print('ERROR: Create project [{}] failed !'.format(project_name))
            return None

    def project_info(self, project_name):
        return self.__get_request('projects?name=' + project_name)

    def delete_project(self, project_name):
        ret = self.project_info(project_name)
        if ret is not None:
            project_id = ret[0].get('project_id')
        else:
            print('ERROR: Can not find project [{}]'.format(project_name))
            return None

        if self.__delete_request('projects/' + str(project_id)):
            return self.project_info(project_name)
        else:
            print('ERROR: Delete project [{}] failed !'.format(project_name))
            return None

    def systeminfo(self):
        return self.__get_request('systeminfo')
        

if __name__ == '__main__':
    a = HarborAPI('hub.kellan.com', 'admin', 'Harbor12345', 'v2.1.0', 'http')
    ret = a.delete_project('test2')
    print(ret)