# -*- coding=utf-8 -*-

import sys

import BeautifulSoup
import requests
import urllib2

from settings import header

reload(sys)
sys.setdefaultencoding('utf-8')


def get_page(url):
    """ 获取网页源码,若网页打开,则获取源码,否则返回None """

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
    page = urllib2.urlopen(req)

    if page and page.getcode() == 200:
        soup = BeautifulSoup.BeautifulSoup(page.read())
        return soup

    return None


def get_page_url(url):
    """ 通过解析网页源码来获取页面内的所有链接 """
    page = get_page(url)
    page_urls = set()

    # 网页获取失败的情况
    if not page:
        return None

    for x in page.findAll('a', href=True):
        url = x.get('href', '')
        if not url or url == '#' or url == '/':
            pass
        if url.startswith('http:'):
            page_urls.add(url)
        else:
            if not url.startswith('javascript'):
                page_urls.add('http://m.sohu.com' + url)

    return page_urls


def get_all_urls(start_url, n=2):
    """ 获取全部链接,n代表获取到几级页面,后期考虑多线程去爬 """
    urls = dict()
    all_urls = set()

    for i in xrange(n):
        urls[str(i)] = set()
        if i == 0:
            urls[str(0)].update(get_page_url(start_url))
            all_urls.update(get_page_url(start_url))
        else:
            for url in urls[str(i-1)]:
                if not get_page_url(url):  # 非空
                    urls[str(i)].update(get_page_url(url))
                    all_urls.update(get_page_url(url))

    return all_urls
