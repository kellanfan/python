# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   55-利用onetimepass做二次认证.py
@Time    :   2019/07/22 09:14:36
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import onetimepass as otp 
import base64
import os
otp_secrit= base64.b32encode(os.urandom(10)).decode('utf-8')
code = otp.get_totp(otp_secrit)
print(code)