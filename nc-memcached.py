#!/usr/bin/python

import os
import logging
nodes = ['a', 'b', 'c']
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='nc-memcache.log',
                    filemode='w')
def getnum(s):
    l = s.read().split(' ')
    num = l[-1]
    return int(num)


for node in nodes:
    cmd_used = 'echo "stats"| nc %s 11211|grep bytes_written' %node
    cmd_total = 'echo "stats"| nc %s 11211|grep limit_maxbytes' %node
    used = os.popen(cmd_used)
    total = os.popen(cmd_total)
    used_byte = getnum(used)
    total_byte = getnum(total)
    free_byte = total_byte - used_byte
    if free_byte < 1000:
        cmd = 'ssh %s /etc/init.d/memcached restart' %node
        msg = '%s node memcached is full...' %node
        logging.warning(msg)
        os.system(cmd)
    else:
        ok_msg =  '%s is ok...' %node
        logging.info(ok_msg)
