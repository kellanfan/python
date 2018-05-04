#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import re
import time
import which_is_sunday

def getreq(url):
    '''构建请求'''
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    return req
    
def gethtml(url):
    '''发送请求，取得返回数据'''
    try:
        page = urllib2.urlopen(url)
        html = page.read()
    except:
        html = None
    finally:
        return html

def main():
    #构建url
    url_head = 'http://www.runningman-fan.com/'
    url_end = '-zz.html'
    week_list = which_is_sunday.sunday()
    #初始化最终的list
    info_list = []

    for part in week_list:
        #构建最终的url
        url = url_head + str(part) + url_end
        #构建请求
        req = getreq(url)
        #正则匹配
        html_reg = re.compile(r'<a href="(https://pan.baidu.com/s/\w*)')
        pass_reg = re.compile(r'密码：(\w*)')
        #获取数据
        html = gethtml(req)
        info = []

        if html != None:
            password = list(set(re.findall(pass_reg, html)))
            html = re.findall(html_reg, html)
            info = tuple(html + password)
            if len(info) == 2:
                r = getreq(info[0])
                html_pan = gethtml(r)
                if r'链接不存在' not in html_pan:
                    print info
                    info_list.append(info)
        time.sleep(0.5)
        

    print info_list


if __name__ == '__main__':
    main()
