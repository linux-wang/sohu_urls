# -*- coding=utf-8 -*-

import datetime
import sys

from test_url import multi_process, process_url

reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    start_url = 'http://m.sohu.com'
    begin = datetime.datetime.now()
    multi_process(start_url, 8)  # 此处参数可以调节线程数
    # process_url(start_url)
    end = datetime.datetime.now()
    print u"用时: ", end - begin
