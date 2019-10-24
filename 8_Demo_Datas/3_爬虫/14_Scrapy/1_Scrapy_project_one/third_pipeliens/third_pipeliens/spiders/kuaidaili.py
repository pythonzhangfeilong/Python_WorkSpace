# -*- coding: utf-8 -*-
import scrapy
from ..items import ThirdPipeliensItem

class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/ops/']

    def parse(self, response):
        item=ThirdPipeliensItem()
        res=response.xpath('//*[@id="freelist"]/table/tbody/tr')
        for var in res:
            ip=var.xpath('.//td/text()')[0].extract()
            port=var.xpath('.//td/text()')[1].extract()
            addr=var.xpath('.//td/text()')[5].extract()
            sudu=var.xpath('.//td/text()')[6].extract()
            order_time=var.xpath('.//td/text()')[7].extract()

            # 等号左边的字段就是items中添加的字段，等号右边为匹配出的内容
            item['ip']=ip
            item['port'] = port
            item['addr'] = addr
            item['sudu'] = sudu
            item['order_time'] = order_time

            # 逐一返回
            yield item