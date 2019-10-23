# 1、scrapy的安装注意事项
'''
    在安装scrapy的时候有依赖的包，先安装Pywin32，在安装twisted
    安装好俩个依赖的包的时候在pip　install scrapy
    import twisted
    import scrapy

    在cmd窗口下去使用scrapy获取网页信息
    scrapy shell http://image.so.com/zjl?ch=beauty&sn=30&listtype=new&temp=1

    import json
    res=json.loads(response.body.decode('utf-8'))
    res

    这样就会把网页的信息展示出来
'''

# 2、scrapy的配置
'''
    创建好项目之后
        第一步：配置settings
            1、ROBOTSTXT_OBEY机器人协议由True改为False
                ROBOTSTXT_OBEY = False
            2、ITEM_PIPELINES由注释改为未注释，拍图片的话，把下面的那个一句加上
                ITEM_PIPELINES = {
                   # 'so_images.pipelines.SoImagesPipeline': 300,
                    'scrapy.pipelines.images.ImagesPipeline':1,
                }
            3、IMAGES_STORE图片的文件夹，不用的话不配置
                IMAGES_STORE='downlaod_iamges'
        第二步：编写items文件
            class SoImagesItem(scrapy.Item):
                # 等于号前面的就是在主目录编写爬虫时创建py文件的name名字，后面的不要动
                image_urls = scrapy.Field()
                pass
        第三步：编写在爬虫主目录中自己的需要的代码
        
        第四步：创建run文件执行
            # 导入cmd执行模块
            from scrapy import cmdline
            # 编写执行语句,crawl后面跟的是爬虫根目录下文件代码中的名字
            cmdline.execute('scrapy crawl baidu'.split())
'''


