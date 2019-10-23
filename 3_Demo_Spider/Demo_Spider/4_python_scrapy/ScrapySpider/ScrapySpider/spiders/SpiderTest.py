#coding:utf-8
import scrapy
#scrapy 本身已经定义好了爬虫请求的结构，我们只需要继承和重写
class TestSpider(scrapy.spiders.Spider):
    """
        TestSpider 我们定义的爬虫类
        scrapy.spiders.Spider 是scrapy定义好的爬虫
    """
    name = "baiduSpider" #定义爬虫的名称
    allowed_domains = [
        "https://www.baidu.com"
    ] #允许爬取的范围
    start_urls = [
        "https://www.baidu.com"
    ] #默认爬取的起始点
    def parse(self,response):
        """
        scrapy 会自动调用downloader的下载器，当请求成功scapy会自动调用parse，
        将结果返回到parse的response参数上
        :param response:
        :return:
        """
        self.log(response.body.decode()) #调试方法在是scrapy当中可以代替print


'''
    上面完成了scrapy的编写，然后执行项目
    scrapy命令在scrapy项目中和项目外的参数不同
    list list是代表列出所有爬虫
    crawl代表执行爬虫
'''




















