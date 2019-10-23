# Scrapy创建爬虫项目的步骤
'''
第一步:
    1、进入创建项目的文件夹中打开cmd窗口
    2、输入scrapy startproject Scrapy_Spider创建Scrapy_Spider这个项目
    3、执行成功后输入cd Scrapy_Spider进入到项目文件夹中
    4、上面的行成功后输入scrapy genspider image image.so.com创建爬虫py文件并且会把爬去的网址参数自动的创建
'''

'''
第二步：
    1、在爬虫项目的根文件夹中找到settings.py文件，找到第22行，把ROBOTSTXT_OBEY = True修改为ROBOTSTXT_OBEY = False
    2、找到第67行ITEM_PIPELINES，把注释取消掉，把原有的'Scrapy_Spider.pipelines.ScrapySpiderPipeline': 300,注释掉，
        新添加'scrapy.pipelines.images.ImagesPipeline': 1,
    3、在ITEM_PIPELINES插入IMAGES_STORE='downlaod_iamges'，创建爬取图片的文件夹
'''

'''
第三步：
    1、在爬虫项目文件夹中找到items.py，把里面的内容修改为
    import scrapy
    class ScrapySpiderItem(scrapy.Item):
        # define the fields for your item here like:
        name = scrapy.Field()
        pass
'''

'''
第四步：
    1、在spiders文件夹中找到刚才创建的爬虫文件images.py写入：
    import scrapy
    import json
    
    class ImagesSpider(scrapy.Spider):
        BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
        name = 'images'
        start_index = 0
        allowed_domains = ['image.so.com']
        start_urls = ['http://image.so.com/zj?ch=art&sn=0&listtype=new&temp=1']
        MAX_DOWNLOAD_NUM = 1000
        def parse(self, response):
            infos = json.loads(response.body.decode('utf-8'))
            # images = SoImagesItem()
            images_list = []
            # images['image_urls'] =
            yield {'image_urls':[info['qhimg_url']for info in infos['list']]}
            self.start_index += infos['count']
            if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
                yield scrapy.Request(self.BASE_URL%self.start_index)
'''

'''
第五步：
    1、在项目的最外层文件夹中创建一个run.py，写入下面的内容，用于启动Scrapy项目
        from scrapy import cmdline
        # 调用执行命令
        cmdline.execute('scrapy crawl images'.split())
'''




















