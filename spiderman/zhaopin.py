# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   zhappin.py
@Time    :   2020/04/13 20:08:07
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import requests
import argparse
import time
import random
from misc.pg_client import Mypostgres
from log.create_logger import create_logger

logger = create_logger()

class ZPspider(object):
    def __init__(self,zhiwei):
        self.pg_client = Mypostgres()
        self.zhiwei = zhiwei
        self.sql = "insert into zhaopin(positionname, workyear, salary, city, education, positionadvantage, companylabellist, financestage, companysize, industryfield, firsttype) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.urls = 'https://www.lagou.com/jobs/list_{}/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput='.format(str(self.zhiwei).encode("utf-8").decode("latin1"))
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': self.urls,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
        }

    def get_cookie(self):
        mysession = requests.Session()
        # 获取搜索页的cookies
        mysession.get(self.urls, headers=self.headers, timeout=3)
        # 为此次获取的cookies
        cookie = mysession.cookies
        return cookie

    def crawler(self):
        cookie = self.get_cookie()
        page = 0
        totalCount = 1
        resultSize = 0
        while (page * resultSize) <= totalCount:
            page = page + 1
            url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

            datas = {
                'first': 'false',
                'pn': page,
                'kd': self.zhiwei
            }
            if page == 1:
                datas['first'] = 'true'

            html = requests.post(url, headers=self.headers, data=datas, cookies=cookie, timeout=5)
            result = html.json()
            if page == 1:
                totalCount = result['content']['positionResult']['totalCount']
                resultSize = result['content']['positionResult']['resultSize']

            jobs = result['content']['positionResult']['result']
            for job in jobs:
                job_array = [job['positionName'], job['workYear'], job['salary'], job['city'], job['education'],
                                job['positionAdvantage'], "|".join(job['companyLabelList']),
                                job['financeStage'], job['companySize'], job['industryField'], job['firstType']]

                # 存入数据库
                code = self.pg_client.execute(self.sql, job_array)
                if code:
                    logger.info('[{}] ok'.format(job_array))
                else:
                    logger.error('[{0}] error, message: [{1}]'.format(job_array,code))

            r = random.randint(15, 30)
            time.sleep(r)

def main(args):
    a = ZPspider(args.zhiwei)
    a.crawler()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-z', '--zhiwei', help='职位信息', action="store", required=True)
    main(parser.parse_args())