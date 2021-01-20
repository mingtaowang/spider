# -*- coding: utf-8 -*-

import gzip

from urllib import request

# urllib是python自带的网络连接库
if __name__ == '__main__':
    # url = 'http://www.baidu.com'
    # response = request.urlopen(url)
    # print(response.info())
    # print(response.getcode())
    # print(type(response))
    # print(response.read())  # b''说明打印输出是字节，
    # print(response.read().decode('utf-8'))  # 解码

    url = 'http://www.qq.com'
    response = request.urlopen(url)
    # print(response.info())  # Accept-Encoding是压缩文件
    response_read = response.read()
    data = gzip.decompress(response_read)   # 解压缩
    print(data.decode('gbk'))    # charset=GB2312，gbk文件，解码
