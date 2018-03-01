#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 01 Mar 2018 03:23:23 PM CST

# File Name: 14-backupfolder.py
# Description:

"""
from multiprocessing import Manager, Pool
import os

def copy_file_content(name, oldFolderName, newFolderName, queue):
    """拷贝单个文件内容"""
    fr = open(oldFolderName + '/' + name)
    fw = open(newFolderName + '/' + name, 'w')
    fw.write(fr.read())
    fr.close()
    fw.close()
    queue.put(name)

def main():
    #获取需要备份的目录
    oldFolderName = input("请输入需要备份的目录：")
    #创建备份目录
    newFolderName = oldFolderName + "-bak"
    os.mkdir(newFolderName)
    #获取源目录中的文件名列表
    filenames = os.listdir(oldFolderName)
    #通过多进程的方式拷贝文件
    filenames_queue = Manager().Queue()
    process_pool = Pool(5)
    for name in filenames:
        process_pool.apply_async(copy_file_content, args=(name, oldFolderName, newFolderName, filenames_queue))

    num = 0
    allnum = len(filenames)
    while True:
        filenames_queue.get()
        num += 1
        rate = num/allnum
        print("\r当前备份进度为：%.2f%%"%(rate*100), end="")
        if num == allnum:    
            break

    process_pool.close()
    process_pool.join()

if __name__ == '__main__':
    main()
