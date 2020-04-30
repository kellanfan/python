# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   proxys.py
@Time    :   2020/04/28 21:44:22
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
from .openurl import MyUserAgent

# 请求获取代理地址
def spider_proxyip(num=10):
    try:
        proxys = []
        headers = dict()
        ua = MyUserAgent()
        headers['User-Agent'] = ua.uarandom()
        url = 'http://www.xicidaili.com/nt/1'
        # 获取代理 IP 列表
        req = requests.get(url, headers=headers)
        source_code = req.content
        # 解析返回的 html
        soup = BeautifulSoup(source_code, 'lxml')
        # 获取列表行
        ips = soup.findAll('tr')

        # 循环遍历列表
        for x in range(1, len(ips)):
            ip = ips[x]
            tds = ip.findAll("td")
            proxy_host = "{0}://".format(tds[5].contents[0]) + tds[1].contents[0] + ":" + tds[2].contents[0]
            proxy_temp = {tds[5].contents[0]: proxy_host}
            # 添加到代理池
            proxys.append(proxy_temp)
            if x >= num:
                break
        return proxys
    except Exception as e:
        print("获取代理地址异常:")
        print(e)