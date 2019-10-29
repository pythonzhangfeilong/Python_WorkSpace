# -*- coding: utf-8 -*-
import scrapy
from ..items import KuaiSpiderItem

class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free']

    def parse(self, response):
        proxy_list=response.xpath('//*[@id="list"]/table/tbody/tr')
        for var in proxy_list:
            item = KuaiSpiderItem()

            IP=var.xpath('.//td/text()')[0].extract()
            PORT=var.xpath('.//td/text()')[1].extract()
            # 匿名度
            Anonymity=var.xpath('.//td/text()')[2].extract()
            # 类型
            type=var.xpath('.//td/text()')[3].extract()
            # 位置
            position=var.xpath('.//td/text()')[4].extract()
            # 响应时间
            response_time=var.xpath('.//td/text()')[5].extract()
            # 最后验证时间
            Last_validation_time=var.xpath('.//td/text()')[6].extract()
            # print(IP,PORT,Anonymity,type,position,response_time,Last_validation_time)

            item['IP'] = IP
            item['PORT'] = PORT
            item['Anonymity'] = Anonymity
            item['type'] = type
            item['position'] = position
            item['response_time'] = response_time
            item['Last_validation_time'] = Last_validation_time
            item.save()
            yield item

        url='http://www.kuaidaili.com/free/inha/%s/'
        for i in range(2,11):
            full_url=url%i
            yield scrapy.Request(url=full_url,callback=self.parse)
