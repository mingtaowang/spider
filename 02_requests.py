# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
    # get请求
    url = 'http://www.httpbin.org/get'
    response = requests.get(url=url)
    print(response.text)
    print(response.encoding)
    print(response.headers)

    # post请求
    url = 'http://www.httpbin.org/post'
    response = requests.post(url=url, data={'name': 'wmt', 'id': 92})
    print(response.text)
    print(response.content)
    print(response.headers)

    url = 'https://n.sinaimg.cn/front/215/w580h435/20181222/BpCV-hqqzpku1671021.jpg'
    response = requests.get(url=url)
    with open('./pictures/cat.jpg', mode='wb') as fp:
        content = response.content  # content为内容的二进制
        fp.write(content)
        print('图片保存成功')

    url = 'https://tieba.baidu.com/p/7138577846?pn={pn}'
    for i in range(10):
        response = requests.get(url=url.format(pn=i+1))
        html = response.text    # 文本数据
        with open('./post_bar/%d.html' % (i+1), mode='w', encoding='utf-8') as fp:
            fp.write(html)
            print('post_bar的第%d数据保存成功' % (i+1))
