#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 10 Jan 2018 10:40:21 AM CST

# File Name: test.py
# Description:

"""

import os, Queue, time
from utils import *
curdir = os.getcwd()
job_id_file = curdir + 'conf/job_id'
vm_queue = Queue.Queue(maxsize = vm_count())
job_status_queue = Queue.Queue(maxsize = vm_count())
put_queue(get_file_content(curdir+'/list/vm_list'), vm_queue)
print "共需要迁移虚机 %d 台" % vm_queue.qsize()

print "首先迁移5台虚机..."
i = 0
while i<5:
    #instance = vm_queue.get()
    job_id = migrate_one_instance(vm_queue.get())
    write_jobid_2_file(job_id_file, job_id)
    i += 1
time.sleep(360)
while True:
    check_job_status(job_id_file, job_status_queue)
    if not job_status_queue.empty():
        n = job_status_queue.qsize()
    write_jobid_2_file(job_id_file, migrate_one_instance(vm_queue.get()))
