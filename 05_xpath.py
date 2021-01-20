# -*- coding: utf-8 -*-

from lxml import etree

if __name__ == '__main__':
    # xpath可以解析网页中的内容，html或者xml类型的文件都是<>开头结尾，层次非常明显
    # data = '''<div>
    #     <ul>
    #         <li class="item-0"><a href="http://www.baidu.com">百度</a></li>
    #         <li class="item-1"><a href="http://www.baidu.com">百度</a></li>
    #     </ul>
    # </div>
    # '''
    # tree = etree.HTML(data)
    # print(type(data))
    # print(tree, type(tree), etree.tostring(tree).decode('utf-8'), sep='\n')     # sep，一行打印一个数据
    # result = tree.xpath('//li')  # //，查找所有li
    # for i in result:
    #     print('--------', etree.tostring(i).decode('utf-8'))

    # result = tree.xpath('/html/body/div/ul/li')     # / ，查找当前路径
    # for r in result:
    #     print('===', etree.tostring(r).decode('utf-8'))

    # class是标签的属性，xpath中用@表示属性
    # result = tree.xpath('//li[@class="item-0"]')    # 查询所有，//；查li，li；表示条件[]
    # for r in result:
    #     print('--------', etree.tostring(r).decode('utf-8'))

    # result = tree.xpath('//a')
    # for r in result:
    #     print('--------', etree.tostring(r).decode('utf-8'))

    # 获取a中文本内容
    # result = tree.xpath('//a/text()')
    # print(result)

    # result = tree.xpath('//li[contains(@class, "0")]')  # 提取出数据所有li中class属性包含0的元素
    # for r in result:
    #     print('--------', etree.tostring(r).decode('utf-8'))

    tree = etree.parse('./data.html')
    # print(etree.tostring(tree, encoding='utf-8').decode('utf-8'))
    # result = tree.xpath('//li[@id="hehe"]/text()')
    # print(result)

    result = tree.xpath('//div[@id="p"]//li')
    for r in result:
        print('--------', etree.tostring(r, encoding='utf-8').decode('utf-8'))

