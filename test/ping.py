#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, netaddr, sys, subprocess

def is_addr(ip_addr):
    try:
        netaddr.IPAddress(ip_addr)
    except:
        return False
    return True

def is_own_ip():
    local_address = []
    for dev in os.listdir('/sys/class/net'):
        if not dev.startswitch('eth'):
            continue
        p = subprocess.Popen("/sbin/ip addr show %s | awk '/inet / {print $2}' | cut -d/ -f 1" % dev , shell=True, stdout=subprocess.PIPE)
        local_ip = p.stdout.read()
        local_ip = local_ip.strip()
        if local_ip:
            if is_addr(local_ip):
                local_address.append(local_ip)
    return sorted(local_address)
    

def ping(ip_addr,ipadd_file):
    local_add = is_own_ip()
    leth = len(local_add)
    i = 0
    while (i < leth):
        if ip_addr is not local_add[i]:
            b = subprocess.call("ping -c 1 -w 1 %s > /dev/null" % ip_addr, shell=True)
            if b == 0:
                try:
                    with open("ipadd_file", "w") as f:
                        f.write("%s" % ip_addr)
                        f.close()
                except:
                    pass
        i += 1
        print ip_addr

if len(sys.argv) != 2:
    sys.exit(-1)

#ipadd_file = sys.argv[1].strip()
if __name__ == "__main__":
    ping(ip_addr,ipadd_file)
