# -*- coding: utf-8 -*-
#####get请求
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
#
# class ScrapySpiderSpider(scrapy.Spider):
#     name = 'baidu'
#     def start_requests(self):
#         url='https://www.baidu.com'
#         headers={'User-Agent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')# 默认是get方法
#     def parse(self, response):
#         select=Selector(response)
#         self.log(select)

#####Xpath匹配
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
#
# class ScrapySpiderSpider(scrapy.Spider):
#     name = 'baidu_Xpath'
#     def start_requests(self):
#         url='https://www.baidu.com'
#         headers={'User-Agent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')# 默认是get方法
#     def parse(self, response):
#         select=Selector(response)
#         img_list = select.xpath("//img/@src")
#         print(type(img_list))  ##<class'scrapy.selector.unified.SelectorList'>
#
#         for img in img_list:
#             self.log(img)

##### css
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
# class BaiduSpider(scrapy.Spider):
#     name='baidu_css'
#     def start_requests(self):
#         url='https://www.baidu.com'
#         headers={'User-Agent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     def parse(self,response):
#         select=Selector(response)
#         img_list=select.css('img')
#
#         for img in img_list:
#             self.log(img)

##### re正则匹配(匹配不出来)
# 正则表达式在scrapy中比较尴尬，不可以独立使用，只能加载匹配项后面
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
#
# class BaiduSpider(scrapy.Spider):
#     name='gif_re'
#     def start_requests(self):
#         url='http://www.gif5.net/'
#         headers={"Referer": "https://www.baidu.com/link?url=dW2F8FcLKkCF62nEciiyg5MStOXGkdlO9gwE0Y5kRzi&wd=&eqid=90fd75130006063b000000035bf5092c",'User-Agent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     def parse(self, response):
#         select=Selector(response)
#         img_list=select.xpath('//img/@src')
#         for img in img_list:
#             Img_re=img.re("(.*?)gif$")
#             self.log(Img_re)

#####Selector对象返回字符结果的方法，Extract
import scrapy
from scrapy.selector import Selector
from fake_useragent import UserAgent
class BaiduSpider(scrapy.Spider):
    name = 'baidu_Extract'
    def start_requests(self):
        url='https://www.baidu.com'
        headers={'User-Agent':UserAgent().random}
        yield scrapy.Request(url=url,headers=headers,method='GET')
    def parse(self, response):
        select=Selector(response)
        img_list=select.xpath('//img/@src')

        for img in img_list:
            Img_Extract=img.extract()
            self.log(Img_Extract)




















