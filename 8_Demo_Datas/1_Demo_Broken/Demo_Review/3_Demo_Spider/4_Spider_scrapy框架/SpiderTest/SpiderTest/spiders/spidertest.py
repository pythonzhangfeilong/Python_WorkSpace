import scrapy
from scrapy import Request
from fake_useragent import UserAgent
class TestSpider(scrapy.spiders.Spider):
    # 爬虫项目的名字，也就是run.py中启动命令时的SpiderName
    name='baiduspider'

    def start_requests(self):
        url='https://www.baidu.com'
        headers={'User-Agent':UserAgent().random}
        yield Request(url,headers=headers)

    def parse(self,response):
        self.log(response.body.decode())




















