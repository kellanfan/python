#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 20 Apr 2018 09:21:28 AM CST

# File Name: 08-MyWebFrameWork.py
# Description:

"""
import time
HTML_ROOT_DIR = '.'

class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO")
        if path.startswith("/static"):
            try:
                f = open(HTML_ROOT_DIR + path)
            except:
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "Not Found"
            else:
                file_data = f.read()
                f.close()

                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url, handler in urls:
            if path == url:
                return handler(env, start_response)
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"

def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ('Server', 'My Server')
    ]
    start_response(status, headers)
    return time.ctime()

def sayhello(env, start_response):
    status = "200 OK"
    headers = [
            ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello haha"


urls = [
    ("/", show_ctime),
    ("/show_ctime", show_ctime),
    ("/sayhello", sayhello)
    ]
app = Application(urls)
