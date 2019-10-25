# -*- coding: utf-8 -*-
import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']

    # 由于Scrapy项目自动创建的时候是为一个get请求，所以使用POST请求就需要将下面的内容全部注释
    # start_urls = ['http://fanyi.baidu.com/']
    # def parse(self, response):
    #     print(response.text)

    # POST请求指定使用的方法
    def start_requests(self):
        # 由于本次爬取的百度翻译是一个局部刷新的网页，也就是一个异步请求，在XHR中重新找url
        post_url='https://fanyi.baidu.com/sug'

        s_data=input('请输入翻译的内容:')
        data={
            'kw':s_data
        }
        yield scrapy.FormRequest(url=post_url,callback=self.get_info,formdata=data)
    # 解析页面内容
    def get_info(self,response):
        import json
        res=json.loads(response.text)
        fanyi_data=res['data'][0]['v']
        print(fanyi_data)







