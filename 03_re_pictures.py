# -*- coding: utf-8 -*-

import re
import requests


if __name__ == '__main__':
        url_first = 'https://sc.chinaz.com/tupian/shanshuifengjing.html'

        # 所有数据
        response = requests.get(url=url_first)
        # with open('./data.html', mode='w', encoding='utf-8') as fp:
        #     fp.write(response.text)
        #     print('网页内容保存成功')

        # 想要数据
        # ？表示非贪婪模式（遇到第一个"就停止），贪婪模式会一路匹配下去
        pattern = r'<img src2="(.*?)" .*?>'   # .表示任意字符，*表示零个或多个,写了()，只会返回()中的内容
        html = response.text
        img_urls = re.findall(pattern, html)
        base = 'http:'
        for img in img_urls:
            img_url = base + img
            response = requests.get(url=img_url)
            content = response.content
            img_name = img_url.rsplit('/', maxsplit=1)[-1]
            with open('./pictures/%s' % img_name, mode='wb') as fp:
                fp.write(content)
