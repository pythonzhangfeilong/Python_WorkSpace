# -*- coding: utf-8 -*-
import scrapy
from ..items import BianProjectItem

class BianSpider(scrapy.Spider):
    # 项目名字
    name = 'bian'
    # 允许爬取的域名
    allowed_domains = ['www.netbian.com']
    # 请求的网址
    start_urls = ['http://www.netbian.com/keai/index.htm']
    def parse(self, response):

        # 注意实例的时候记的后面加括号
        item=BianProjectItem()
        res=response.xpath('//div[@class="list"]/ul/li')

        for var in res:
            img_name = var.xpath('.//a/b/text()').extract_first()
            img_url=var.xpath('.//a/img/@src').extract_first()
            item['img_name'] = img_name
            item['img_url'] =img_url

            yield item

        base_url='http://www.netbian.com/keai/index_%s.htm'

        for ye_data in range(2,6):
            full_url=base_url%ye_data
            print(full_url)
            # scrapy请求，是一个回调函数
            yield scrapy.Request(url=full_url,callback=self.parse)