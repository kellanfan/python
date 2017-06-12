#!/usr/bin/python
#-*- coding:utf-8 -*-

import socket, time, thread

socket.setdefaulttimeout(3)  #默认超时时间

def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否占用
    """

    try:
        if port:
            print u'端口扫描结束'
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print ip,u':', port,u'端口已被占用'
            lock.release()
    except:
        print u'端口扫描异常'

def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """

    try:
        print u'开始扫描 %s' % ip
        start_time=time.time()
        for i in range(0,65534):
            thread.start_new_thread(socket_port,(ip, int(i)))
        print u'扫描端口完成，总用时: %.2f' %(time.time()-start_time)
    except:
        print u'扫描IP异常'

if __name__ == '__main__':
    org=raw_input('Input the ip you want to scan: ')
    lock=thread.allocate_lock()
    ip_scan(org)
