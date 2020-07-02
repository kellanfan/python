#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 21 Aug 2018 02:09:47 PM CST

# File Name: douban_movie_shortcomment.py
# Description:

"""
import re
import time
import sys
from bs4 import BeautifulSoup
from misc.openurl import OpenUrl


class Spider(object):
    def __init__(self,movie_id):
        self.movie_id = movie_id
        self.base_url = 'https://movie.douban.com/subject/%s/comments' %movie_id
        self.start_url = 'https://movie.douban.com/subject/%s/comments?status=P' %movie_id
        self.python_version = sys.version_info[0]
    def _get_content(self,url):
        ourl = OpenUrl(url)
        code, content = ourl.run()
        if code == 200:
            return content
        else:
            return None

    def _save_tmp_file(self,content):
        filename = self.movie_id + '.txt'
        with open(filename, 'a+') as f:
            f.write(content + '\n')
            
    def _get_data(self, content):
        soup = BeautifulSoup(content, 'lxml')
        for short in soup.find_all('span',class_="short"):
            soup1 = BeautifulSoup(str(short))
            short_comment = soup1.span.string
            self._save_tmp_file(short_comment)
        try:
            soup_next = BeautifulSoup(str(soup.find_all('a', class_='next')))
            return soup_next.a['href']
        except:
            return None

    def run(self):
        if self.python_version != 3:
            print('Use python3')
            sys.exit(-1)
        next_url = ''
        current_url = self.start_url
        while True:
            content = self._get_content(current_url)
            time.sleep(0.5)
            if content is None:
                break
            next_url = self._get_data(content)
            if next_url is None:
                break
            current_url = self.base_url + next_url
            print(current_url)
            
if __name__ == '__main__':
    a = Spider('26985127')
    a.run()
