# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   21-远程执行命令.py
@Time    :   2020/10/26 15:50:58
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
#!/usr/bin/env python3

import paramiko
import sys
class RemoteCmd(object):
    def __init__(self, hostname, port, username, auth_mode='pass', passwd=None, key_filename=None):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.auth_mode = auth_mode
        self.passwd = passwd
        self.key_filename = key_filename
        self.check_parse()

    def check_parse(self):
        if self.auth_mode not in ('pass', 'key'):
            print('ERROR: Auth Mode is invalid, must be in [pass, key].')
            sys.exit(1)

        if self.auth_mode == 'pass' and self.passwd is None:
            print('ERROR: Please provide the password !')
            sys.exit(1)
        elif self.auth_mode == 'key' and self.key_filename is None:
            print('ERROR: Please provide the Key !')
            sys.exit(1)
            
    def exec_cmd(self, cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.auth_mode == 'pass':
                client.connect(hostname=self.hostname,
                           port=self.port,
                           username=self.username,
                           password=self.passwd)
            elif self.auth_mode == 'key':
                client.connect(hostname=self.hostname,
                           port=self.port,
                           username=self.username,
                           key_filename=self.key_filename)
        except Exception as e:
            print("ERROR: Connect to [{0}] Failed: [{1}]".format(self.hostname, e))
        else:
            print("Execing [{0}] with [{1}] ...".format(self.hostname, cmd))
            _, stdout, stderr = client.exec_command(cmd)
            result = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            if error.strip():
                return error
            else:
                return result
        finally:
            client.close()