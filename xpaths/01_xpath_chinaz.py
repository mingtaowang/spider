# -*- coding: utf-8 -*-

import time
import requests

from lxml import etree

if __name__ == '__main__':
    url_first = 'https://sc.chinaz.com/tupian/index.html'
    url_backend = 'https://sc.chinaz.com/tupian/index_%d.html'
    url_base = 'http:'
    for i in range(1, 11):
        url = url_first if not i else url_backend % (i + 1)
        response = requests.get(url=url)
        tree = etree.HTML(response.text)
        images = tree.xpath('//img/@src2')  # //代表查找文本中任意的位置；@src2表示获取标签中的属性src2
        images = [url_base + i for i in images]
        for img_url in images:
            response = requests.get(url=img_url)
            img_name = img_url.rsplit('/', maxsplit=1)[-1]
            with open('./images/%s' % img_name, mode='wb') as fp:  # w，写；b，字节；wb，以字节的形式写进去
                fp.write(response.content)
                print('-----图片%s保存成功-----' % img_name)
            time.sleep(1)
