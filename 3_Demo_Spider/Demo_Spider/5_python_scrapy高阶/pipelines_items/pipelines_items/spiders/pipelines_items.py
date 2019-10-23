#####items的使用
# import scrapy                           # 导入scrapy框架
# from scrapy.selector import Selector    # 导入scrapy的匹配核心Selector
# from fake_useragent import UserAgent    # 导入UserAgent随机残生一个浏览器
# from pipelines_items.items import MyspiderItem
# # 创建一个类，并且继承scrapy.spiders.Spider
# class BaiduSpider(scrapy.spiders.Spider):
#     # 创建一个名字，也就是一会run文件中crawl后面的内容
#     name='baidu'
#     # 创建以恶搞方法，里面是请求的内容，并且以生成器的方式返回
#     def start_requests(self):
#         url='https://www.baidu.com'
#         headers={'UserAgent':UserAgent().random}
#         # 以生成器的方式返回，method是请求的方式，默认的是get
#         yield scrapy.Request(url=url,headers=headers,method='GET')
#     # 定义一个方法用来处理响应，设置参数是response
#     def parse(self,response):
#         select=Selector(response)
#         image=select.xpath('//img/@src')
#
#         for i in image:
#             item=MyspiderItem()
#             # 以字节的形式返回
#             item['src']=i.extract()
#             self.log(item)

#####pipelinse的使用
'''
    这是就可以对数据进行格式化了，但是数据的输出还是需要pipelines
    1、使用pipelines的第一步是吧settings当中解开ITEM_PIPELINES的配置
    2、优先级从1到1000，越大越优先下载
'''
# 导入srapy框架
import scrapy
# 导入scrapy的匹配核心Selector
from scrapy.selector import Selector
# 导入UserAgent随机产生浏览器
from fake_useragent import UserAgent
# 创建一个类,继承scrapy.spiders.Spider
from pipelines_items.items import MyspiderItem
class BaiduSpider(scrapy.spiders.Spider):
    # 创建名字，方便在run.py中调用
    name='baidu'
    # 写一个方法用来进行请求，最后以生成器的方式返回
    def start_requests(self):
        url='https://www.baidu.com'
        headers={'User-Agent':UserAgent().random}
        yield scrapy.Request(url=url,headers=headers,method='GET')

    # 创建一个方法，用来处理请求的响应，并且要含带response的参数
    def parse(self,response):
        select=Selector(response)
        images=select.xpath('//img/@src')

        for i in images:
            # 将items中的类实例为对象
            item=MyspiderItem()
            # 取src这个字符串
            item['src']=i.extract()
            # 输出
            self.log(item)
            yield item














