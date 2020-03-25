# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   双色球.py
@Time    :   2020/01/10 08:36:49
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
from lxml import etree
from misc.openurl import OpenUrl
from misc.pg_client import Mypostgres


url = 'http://www.310win.com/shuangseqiu/tubiao_lshm.html'
ourl = OpenUrl(url)
code,doc = ourl.run()
pg_conn = Mypostgres()
s_sql = 'select opendate from shuang_se_qiu order by opendate desc limit 1'
last_time = pg_conn.execute(s_sql)
if code == 200:
    selecter = etree.HTML(doc)
    info_list = selecter.xpath("//span[@id='spnHidValue']/text()")
    for item in info_list[0].split('#'):
        item_info = item.split('+')
        if len(item_info) > 1:
            opendate = item_info[0].split('&')[1]
            issue_num = item_info[1]
            r_nunber, b_number = item_info[2].split('|')
            if opendate > last_time[0][0]:
                sql = "insert into shuang_se_qiu(opendate, issue_num, r_number, b_number) values (%s,%s,%s,%s)"
                ret = pg_conn.execute(sql,[opendate, issue_num, r_nunber,b_number])
                if ret:
                    print("insert [{}] ok..".format(issue_num))
                else:
                    print("insert [{0}] failed: [{1}]".format(issue_num, ret))