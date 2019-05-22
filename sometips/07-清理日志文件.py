# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   freespace.py
@Time    :   2019/05/21 11:09:00
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import os

def get_files(path):
    file_list = []
    for root,files in os.walk(path):
        for name in files:
            file_list.append(os.path.join(root, name))
    return file_list

def clean_file(item):
    file_size = os.path.getsize(item)
    if file_size >= 10240000 and item.endswith('.log'):
        with open(item,'w') as f:
            step = 20480
            while file_size > 0:
                f.seek(0)     
                f.truncate(step)
                file_size -= step

        print('[%s] has been clean..'%item)

def main():
    files_list = []
    dirlist = ['/var/log', '/tmp']
    for dirs in dirlist:
        files_list.extend(get_files(dirs))

    for files in files_list:
        clean_file(files)

    print("clean files done..")

if __name__ == '__main__':
    main()
