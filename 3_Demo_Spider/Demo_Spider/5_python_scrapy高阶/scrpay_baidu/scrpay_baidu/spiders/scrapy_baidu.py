#####scrapy的匹配核心是selector
# import scrapy                           # 导入scrapy模块(其实也就是框架)
# from scrapy.selector import Selector    # 导入的是scrapy框架中的匹配核心Selector
# from fake_useragent import UserAgent    # 导入UserAgent产生随机的浏览器
# # 创建一个类并且继承scrapy.spiders.Spider
# class BaiduSpider(scrapy.spiders.Spider):
#     # 创建爬虫的名字
#     name='baidu'
#     # 创建一个固定的请求方法，包括url、headers以及采用生成起返回scrapy响应的数据,注意这个方法是start_requests有s
#     def start_requests(self):
#         # 请求的url
#         url='https://www.baidu.com/'
#         # 随机产生一个浏览器
#         headers={'User-Agent':UserAgent().random}
#         # 生成器的方式返回scrapy请求的数据，method是请求的方式，默认的是GET请求
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     def parse(self,response):
#         # 使用Selector匹配，下面是匹配的响应内容
#         select=Selector(response)
#         self.log(select)

#####Xpath匹配
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
#
# class BaiduSpider(scrapy.spiders.Spider):
#     name='baidu'
#     def start_requests(self):
#         url='https://www.baidu.com/'
#         headers={'User-Agent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     def parse(self,response):
#         select=Selector(response)
#         image=select.xpath('//img/@src')
#
#         for i in image:
#             self.log(i)

#####re正则匹配
'''
    re正则匹配比较尴尬，它不可以独立使用，只能加在匹配项后面
'''
# import scrapy
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
# class BaiduSpider(scrapy.spiders.Spider):
#     name='baidu'
#     def start_requests(self):
#         url='https://www.baidu.com'
#         headers={'UserAgent':UserAgent().random}
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     def parse(self,response):
#         select=Selector(response)
#         xpath_url="//img/@src"
#         image=select.xpath(xpath_url)
#
#         for i in image:
#             # re匹配，匹配所有
#             IAMGE=i.re('(.*?)gif$')
#             self.log(IAMGE)

#####Selector对象返回字符结果的方法：Extract
import scrapy
from scrapy import Selector
from fake_useragent import UserAgent
class BaiduSpider(scrapy.spiders.Spider):
    name='baidu'
    def start_requests(self):
        url='https://www.baidu.com'
        headers={'User-Agent':UserAgent().random}
        yield scrapy.Request(url=url,headers=headers,method='GET')
    def parse(self,response):
        select=Selector(response)
        image=select.xpath('//img/@src')

        for i in image:
            IMAGE=i.extract()
            self.log(IMAGE)

