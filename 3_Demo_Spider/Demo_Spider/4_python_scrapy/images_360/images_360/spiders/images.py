# -*- coding: utf-8 -*-
import json

import scrapy


class ImagesSpider(scrapy.Spider):
    # 地址中的sn=%s
    BASE_URL='http://image.so.com/zjl?ch=beauty&sn=%s&listtype=new&temp=1'
    name = 'images'
    start_index=0
    allowed_domains = ['image.so.com']
    # 地址中的sn=0
    start_urls = ['http://image.so.com/zjl?ch=beauty&sn=0&listtype=new&temp=1']
    # 最大的下载量
    MAX_DOWNLOAD_NUM=1000
    def parse(self, response):
        # 将返回的json文本转换为python可操作对象
        infos=json.loads(response.body.decode())
        # 与items里面的名字保持一致
        yield {'image_urls':[info['qhimg_url']for info in infos['list']]}
        self.start_index+=infos['count']
        if infos['count']>0 and self.start_index <self.MAX_DOWNLOAD_NUM:
            # 路径拼接，也就是sn的值
            yield scrapy.Request(self.BASE_URL%self.start_index)