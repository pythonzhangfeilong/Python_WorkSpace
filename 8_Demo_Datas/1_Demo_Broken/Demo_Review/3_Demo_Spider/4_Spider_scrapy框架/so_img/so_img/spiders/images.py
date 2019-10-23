# -*- coding: utf-8 -*-
import scrapy


# class ImagesSpider(scrapy.Spider):
#     name = 'images'
#     allowed_domains = ['image.so.com']
#     start_urls = ['http://image.so.com/']
#
#     def parse(self, response):
#         pass


import scrapy
import json
from so_img.items import SoImgItem


class ImagesSpider(scrapy.Spider):
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    name = 'images'
    start_index = 0
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/zj?ch=art&sn=0&listtype=new&temp=1']
    MAX_DOWNLOAD_NUM = 100

    def parse(self, response):
        infos = json.loads(response.body.decode())
        # images = ScrapyspiderItem()
        # images['image_urls']=[info['qhimg_url']for info in infos['list']]
        # yield images

        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)
