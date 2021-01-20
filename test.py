# -*- coding: utf-8 -*-

import re
import requests


if __name__ == '__main__':
    url = 'http://scpic.chinaz.net/Files/pic/pic9/201902/bpic10663_s.jpg'
    files = url.rsplit('/', maxsplit=1)
    print(files)
    print(files[0])
    print(files[1])
    print(files[-1])
    file_name = files[1]
    # print(file_name)
    # print('wmt')
    # print(url.rsplit('/'))
    # print(url.split('/'))
