# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   load-docker-images.py
@Time    :   2020/07/27 12:44:28
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import os
for item in os.listdir('/installer/images'):
    item = os.path.splitext(os.path.basename(item))[0]
    image_name= item.replace('#', '/')
    ret = os.popen('docker load -i /installer/images/{}.tar'.format(item))
    image_id = ret.readlines()[0].strip().split(':')[2]
    ret_code = os.system('docker tag {0} {1}'.format(image_id, image_name))
    if ret_code == 0:
        print("Load image [{}] successful..".format(image_name))
    else:
        print("Load image [{}] failed..".format(image_name))
