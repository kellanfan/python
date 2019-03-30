#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Mar 2019 09:36:35 AM CST

# File Name: 04-urllib2_tieba.py
# Description:

"""
import urllib
import urllib2

def loadPage(url,filename):
    """
        获取url页面内容
        url：爬取的url地址
    """
    print "正在下载" + filename
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    request = urllib2.Request(url, headers = headers)
    return urllib2.urlopen(request).read()

def writePage(html,filename):
    """
        保存页面内容到文件中
    """
    print "正在保存" + filename
    with open(filename, 'w') as f:
        f.write(html)
    print "="*30

def tiebaSpider(tieba,startPage,endPage):
    """
        调度器
    """
    url = "http://tieba.baidu.com/f?"
    kw = urllib.urlencode({"kw":tieba})
    for page in range(startPage, endPage + 1):
        pn = (page - 1)*50
        filename = tieba + "page" + str(page) + '.html'
        fullurl = url + kw + "&pn=" + str(pn)
        html = loadPage(fullurl, filename)
        writePage(html, filename)

if __name__ == '__main__':
    tieba = raw_input("需要爬取的贴吧名：")
    startPage = int(raw_input("起始页："))
    endPage = int(raw_input("结束页："))
    
    tiebaSpider(tieba,startPage,endPage)
