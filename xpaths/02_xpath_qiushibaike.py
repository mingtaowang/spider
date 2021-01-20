# -*- coding: utf-8 -*-

import json
import time
import requests

from lxml import etree

if __name__ == '__main__':
    # 爬虫的底层伪装，伪装成浏览器，网站服务器一般不会禁止浏览器发起的请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Referer': 'https://www.qiushibaike.com/text/',
        'Host': 'www.qiushibaike.com',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    url_first = 'https://www.qiushibaike.com/text/'
    url_backend = 'https://www.qiushibaike.com/text/page/%d/'
    fp = open('./qiushibaike.txt', mode='a', encoding='utf-8')  # a，append，追加
    fp_json = open('./qiushibaike.json', mode='w', encoding='utf-8')
    data = []
    for i in range(1, 14):
        url = url_first if i == 1 else url_backend % i
        response = requests.get(url=url, headers=headers)
        tree = etree.HTML(response.text)
        # 查找div的class属性里面，包含article的div，它底下的div
        divs = tree.xpath('//div[@class="article block untagged mb15 typs_hot"]')
        for div in divs:
            author = div.xpath('.//h2/text()')[0].replace('\n', '')    # .从当前目录下去查找数据
            content = div.xpath('.//span/text()')[0].replace('\n', '')
            laugh = div.xpath('.//i[@class="number"]/text()')
            fp.write('作者：%s。笑话：%s。好笑：%s。评论：%s\n' % (author, content, laugh[0], laugh[1]))
            d = dict()
            d.update(作者=author, 笑话=content, 好笑=laugh[0], 评论=laugh[1])
            data.append(d)
            print(author, content, laugh)
            time.sleep(1)

    fp.close()
    result = json.dumps(data, ensure_ascii=False)
    fp_json.write(result)
    fp_json.close()
