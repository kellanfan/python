# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import os
def gethtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r'data-id="(\d*)" data-seq'
    dataid = re.compile(reg)
    dataidlist = re.findall(dataid, html)
    localdir = os.path.abspath('./image')
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
def get_boards(url):
    html = gethtml(url)
    reg1 = r'"board_id":(\d*)'
    boardid = re.compile(reg1)
    boardid1 = re.findall(boardid, html)
    boardidlist = list(set(boardid1))
    return boardidlist
if __name__ == '__main__':
    boardidlist = get_boards("http://huaban.com/fk674188382/following/")
    print boardidlist
    for boardid in boardidlist:
        board_url = r'http://huaban.com/boards/%s' %boardid
        try:
            html = gethtml(board_url)
        except:
            print ("bad url: %s") % board_url
            continue
        getimg(html)
    html = gethtml("http://huaban.com/boards/735459/")
    getimg(html)
