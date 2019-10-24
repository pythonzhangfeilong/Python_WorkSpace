# -*- coding: utf-8 -*-
import scrapy
from urllib import request
import time
class BianSpider(scrapy.Spider):
    # 爬虫名字
    name = 'bian'
    # 允许爬取的域名
    allowed_domains = ['www.netbian.com']
    # 爬取的地址
    start_urls = []

    for i in range(1,9):
        url='http://www.netbian.com/youxi/index_%d.htm'%i
        start_urls.append(url)

    def parse(self, response):
        for var in range(1,9):
            res=response.xpath('//div[@class="list"]/ul/li/a/img/@src').extract()
            print('第%s页开始'%var)
            print('一共获取到%s张图片，即将开始下载：'%len(res))
            time.sleep(5)
            for img_url in res:
                img_name=img_url.split()[0][-10:]
                print('正在下载的是%s'%img_name)
                request.urlretrieve(url=img_url,filename='./image/%s'%img_name)
                time.sleep(1)
                print('下载完成的是%s' % img_name)
            print('本次下载共%s张图片，马上下载完成，请稍等，正在校验。。。。。'%len(res))
            time.sleep(5)
            print('本次下载服务结束，感谢使用')
            print('第%s页结束' % var)