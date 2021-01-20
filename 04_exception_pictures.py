# -*- coding: utf-8 -*-

import re
import time
import requests

if __name__ == '__main__':
    url_first = 'https://sc.chinaz.com/tupian/index.html'
    url_base = 'https://sc.chinaz.com/tupian/index_%d.html'
    base = 'http:'
    try:
        for i in range(2):
            url = url_first if not i else url_base % (i + 1)
            response = requests.get(url=url)
            html = response.text
            # ？表示非贪婪模式（遇到第一个"就停止），贪婪模式会一路匹配下去
            pattern = r'<img src2="(.*?)" .*?>'  # .表示任意字符，*表示零个或多个,写了()，只会返回()中的内容
            img_urls = re.findall(pattern, html)
            img_urls = [base + i for i in img_urls]
            img_names = [i.rsplit('/', maxsplit=1)[-1] for i in img_urls]
            for img_url, img_name in zip(img_urls, img_names):
                response = requests.get(url=img_url, timeout=10)
                content = response.content
                with open('./chinaz/%s' % img_name, mode='wb') as fp:
                    fp.write(content)
                    print('第{page}页的图片：{name}保存成功'.format(page=i + 1, name=img_name))
                time.sleep(1)
    except Exception as e:
        with open('.exception.txt', 'a', encoding='utf-8') as fp:   # a，追加
            fp.write(str(e) + '\n')
