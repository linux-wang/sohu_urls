# -*- coding=utf-8 -*-
# filename=sohu.py

import datetime
import socket
import sys
import urllib2
from multiprocessing.dummy import Pool as ThreadPool

from get_urls import get_all_urls
from log import save_to_log

reload(sys)
sys.setdefaultencoding('utf-8')

# from multiprocessing import Pool


# or requests.raise_for_status() requests.RequestException
def get_opener(url):
    """ 包装urllib2的请求 """
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
    return req, opener


def is_dead_link(url, n=3):
    """ 判断是否为死链,n代表检测次数, 例如n=2 则访问链接2次,均为死链的时候则判断为死链接 """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print u'正在处理: ' + url
    print '-------------------------'

    if url:
        req, opener = get_opener(url)
        try:
            resp = opener.open(req, timeout=5)
        except urllib2.HTTPError, ex:
            if n > 1:
                is_dead_link(url, n-1)
            else:
                save_to_log(now + ' ' + url + ' ' + str(ex))
        except urllib2.URLError, ex:
            if n > 1:
                is_dead_link(url, n - 1)
            else:
                save_to_log(now + ' ' + url + ' ' + str(ex))
        except socket.timeout as ex:
            if n > 1:
                is_dead_link(url, n - 1)
            else:
                save_to_log(now + ' ' + url + ' ' + str(ex))

    # TODO: 多线程


def process_url(start_url):
    """ 单进程处理 """
    urls = get_all_urls(start_url, 2)
    print len(urls)
    for url in urls:
        is_dead_link(url)


def multi_process(start_url, n=4):
    """ 多进程处理函数 ref: https://segmentfault.com/a/1190000000414339"""
    urls = list(get_all_urls(start_url, 2))
    pool = ThreadPool(n)
    pool.map(is_dead_link, urls)
    pool.close()
    pool.join()
