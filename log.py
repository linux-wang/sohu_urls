# -*- coding=utf-8 -*-

import datetime
import sys

from settings import log_path

reload(sys)
sys.setdefaultencoding('utf-8')


def save_to_log(err_string):
    """ 死链写入日志文件 """
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file_name = today + '.txt'

    with open(log_file_name, 'a') as f:
        f.write(err_string)
        f.write('\t\n')
