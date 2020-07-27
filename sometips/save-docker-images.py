# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   save-docker-images.py
@Time    :   2020/07/27 12:44:35
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import os
cmd1 = """
docker images | grep -v REPOSITORY | awk '{print $1":"$2, $3}'
"""
ret = os.popen(cmd1)
for item in ret.readlines():
    image_name, image_id = item.split()
    image_name = image_name.replace('/', '#').strip()
    ret_code = os.system('docker save {0} > /root/images/{1}.tar'.format(image_id.strip(),image_name))
    if ret_code == 0:
        print("Save image [{}] successful..".format(image_name))
    else:
        print("Save image [{}] failed..".format(image_name))
