# -*- coding: utf-8 -*-
import re

import scrapy                               # 导入scrapy
import requests                             # 导入requests
from fake_useragent import UserAgent        # 导入UserAgent生成随机浏览器
from scrapy.selector import Selector        # Selector是scrapy匹配的核心

class HohhotRealEstateSpider(scrapy.Spider):
    name = 'Hohhot_Real_Estate'
    allowed_domains = ['www.365hf.com']
    start_urls = ['http://www.365hf.com/']
    # 定义一个方法,用于处理请求
    def start_requests(self):

        base_url = 'http://www.365hf.com/newhouse/search-12-0-0-0-0-0-0-0-0-1.html'

        headers = {'User-Agent': UserAgent().random}

    # 使用生成器yield返回请求信息,请求的方式为GET
        yield scrapy.Request(url=base_url,headers=headers,method='GET')

    # 定义一个方法用来处理请求，并且设置参数为response
    def parse(self,response):
        # 匹配响应的请求并且赋给select对象
        select=Selector(response)
        # 匹配处理
        Real_Estate=select.xpath('//div[@class="loupan_list_info"]//div[@class="loupan_tit"]/h3/a/text()')
        #
        data=Real_Estate.extract_first['data']
        print(data)



