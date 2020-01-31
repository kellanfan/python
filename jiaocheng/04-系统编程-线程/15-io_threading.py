# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   15-io_threading.py
@Time    :   2020/01/28 20:44:30
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import concurrent.futures
import requests
import time
import threading
#线程本地存储，会创建一个全局对象但有时特定于每个线程
thread_local = threading.local()
# 使数据访问变成线程安全
def get_session():
    if getattr(thread_local, 'session', None) is None:
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print('Read {0} fom {1}'.format(len(response.content), url))
# ThreadPoolExecutor = Thread + Pool + Executor,Executor是控制线程池中的每个线程如何以及何时运行的部分
# 它实现为一个上下文管理器，因此可以使用with语法来管理进程池的创建和释放。
# map方法在列表中的每个站点上运行传入的参数
def download_all_site(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://www.baidu.com"
    ] * 80
    start_time = time.time()
    download_all_site(sites)
    duration = time.time() - start_time
    print('Download {0} in {1} seconds'.format(len(sites), duration))