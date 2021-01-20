# -*- coding: utf-8 -*-

import json
import time
import requests

from lxml import etree

if __name__ == '__main__':
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%s,2,1.html'
    key = input('请输入查询工作的关键字：')
    url = url % key
    response = requests.get(url=url)
    response.encoding = 'gbk'
    print(response.text)
