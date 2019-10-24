# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 在命令窗口创建的爬虫名字
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 开始爬取的url
    start_urls = ['http://www.baidu.com/']

    # 爬虫启动之后执行的内容
    def parse(self, response):
        print('=======')
        # 获取页面源码
        # print(response.text)

        # 直接进行xpath匹配       因为匹配到的内容是在一个selector对象的data中包含的，所以用extract()获取data中的数据
        print(response.xpath('//*[@id="lg"]').extract())

        # 查看response中的方法
        # print(dir(response))
        print('=======')

