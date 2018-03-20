#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 09 Jan 2018 09:31:33 AM CST

# File Name: utils.py
# Description:

"""
import os, Queue
import subprocess
from random import choice

curdir = os.getcwd()
def get_file_content(filepath):
    with open(filepath) as f:
        m = f.read().split('\n')
        while '' in m:
            m.remove('')
        return tuple(m)

def vm_count():
    count = 0
    with open(curdir + '/list/vm_list','rb') as f:
        while True:
            buffer = f.read(1024*8192)
            if not buffer:
                break
            count += buffer.count('\n')
        return count

def put_queue(list, q):
    for l in list:
        q.put(l)
    return q

def random_get_hyper():
    return choice(get_file_content(curdir + '/list/hyper_list'))

def migrate_one_instance(instance, hyper=random_get_hyper()):
    os.chdir('/pitrix/cli')
    cmd = "./migrate-instances -i %s -t %s"%(instance, hyper)
    for line in subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True).stdout.readlines():
        if "ret_code" in line:
            ret_code = int(line.split(':')[1])
        if "job_id" in line:
            job_id = line.split(':')[1]
    print "ACTION: %s to %s : ret_code: %d  job_id: %s" %(instance, hyper, ret_code, job_id)
    return job_id

def write_jobid_2_file(filepath, jobid):
    with open(filepath,'a') as f:
        f.write(jobid + '\n')

def check_job_status(filepath,q):
    job_id_list = get_file_content(filepath)
    os.chdir('/pitrix/cli')
    for job_id in job_id_list:
        cmd = "./describe_jobs -j %s" %job_id
        for line in subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True).stdout.readlines():
            if "status" in line:
                status = line.split(':')[1]
            if status == 'successful' or status == 'failed':
                job_status = job_id + ':' + status 
                q.put(job_status)
    return q

if __name__ == '__main__':
    write_jobid_2_file('a.txt','aa')

