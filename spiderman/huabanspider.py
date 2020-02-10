# -*- coding: utf-8 -*-
import urllib
import re
import os
from misc.openurl import OpenUrl
from log.create_logger import create_logger
from lxml import etree

logger = create_logger()

def gethtml(url):
    ourl = OpenUrl(url)
    code,html = ourl.run()
    if code != 200:
        html = None
    return html

def getimg(html):
    reg = r'data-id="(\d*)" data-seq'
    dataid = re.compile(reg)
    dataidlist = re.findall(dataid, html)
    localdir = os.path.abspath('image')
    for pinid in dataidlist:
        url_str = r'http://huaban.com/pins/%s/' % pinid
        pin_id_source = gethtml(url_str)
        img_url_re = re.compile('main-image.*?src="(.*?)"',re.S)
        img_url_list = re.findall(img_url_re,pin_id_source)
        try:
            img_url = 'http:' + img_url_list[0]
            if '_fw658' in img_url:  
                img_url = img_url[:-6]
            img_name = img_url[-6:]
            local = os.path.join('%s','%s.jpeg') %(localdir, img_name)
            #urllib.urlretrieve(img_url, '%s.jpeg' % x)
            urllib.urlretrieve(img_url, local)
        except:
            print("can find %s "% img_url)
            continue
        print("获取：%s成功！" % img_url)
    print("图片保存成功！")

def get_users(url):
    selecter = etree.HTML(gethtml(url))
    return selecter.xpath('//a[@class="username"]/@href')

if __name__ == '__main__':
    if not os.path.isdir('image'):
        os.mkdir('image')
    users_list = get_users("https://huaban.com/x8udz9xpqvx/following/")
    print(users_list)

