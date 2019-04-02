#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 01 Apr 2019 09:06:24 AM CST

# File Name: 07-cookielogin.py
# Description:

"""

import urllib2

url = "https://www.douban.com/"
headers = {
	"Connection": "keep-alive"
	"Cookie": "ll="108288"; bid=aV1Zf5O9vTM; _ga=GA1.2.904416647.1526898326; __utmv=30149280.4664; __yadk_uid=vR1HDnDM7jDF08irnqrFY1Wn801oHr6L; _vwo_uuid_v2=D91CC8578B0CA976BF78799D3D0CF6149|b6d9f5dc7cacafb411d27aea0323d9cc; gr_user_id=8c11b6a1-d7af-4a5a-9c3b-fb2758e7d86e; push_doumail_num=0; douban-fav-remind=1; douban-profile-remind=1; push_noty_num=0; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1554078685%2C%22https%3A%2F%2Fwww.baidu.com%2F%22%5D; __utma=30149280.904416647.1526898326.1553752592.1554078687.160; __utmc=30149280; __utmz=30149280.1554078687.160.106.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2=46640706:yfN6frYjVyY; ck=VqMk; ap_v=0,6.0; _pk_id.100001.8cb4=b93a8a74f593c880.1526898324.126.1554078701.1553752475."
	"Host": "www.douban.com"
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

request = urllib2.Request(url, headers = headers)
print urllib2.urlopen(request).read()
