# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from App1.models import Proxy

class KuaiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # IP = scrapy.Field()
    # PORT = scrapy.Field()
    # # 匿名度
    # Anonymity = scrapy.Field()
    # # 类型
    # type = scrapy.Field()
    # # 位置
    # position = scrapy.Field()
    # # 响应时间
    # response_time = scrapy.Field()
    # # 最后验证时间
    # Last_validation_time = scrapy.Field()

    django_modle=Proxy