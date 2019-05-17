# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   04-生成mac地址.py
@Time    :   2019/05/14 16:26:38
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import random

def makeMAC():
    mac = [0x00,0x63,
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)
        ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

if __name__ == '__main__':
    print(makeMAC())