#####利用scrapy爬虫框架，爬去javascript动态加载页，将图片下载到本地
# 1、第一步：创建项目，在指定文件夹下打开cmd窗口输入scrapy startproject images_360,创建images_360的项目

# 2、第二步，在cmd窗口进入images_360的主目录，输入scrapy genspider images image.so.com,使用scrapy固定模板

# 3、第三步：配置settings文件，关闭robots协议
'''
    ROBOTSTXT_OBEY = False
    # 在setting文件的下面
    ITEM_PIPELINES = {
        # 'so_images.pipelines.SoImagesPipeline': 300,
        'scrapy.pipelines.images.ImagesPipeline':1,
}
    需要自己创建，也就是下载图片的文件
    IMAGES_STORE='downlaod_iamges'
'''
# 4、第四步：编写items文件
'''
    class SoImagesItem(scrapy.Item):
        # define the fields for your item here like:
        image_urls = scrapy.Field()
        pass
'''
# 5、第五步：spider中images的编写(最重要)

# 6、第六步：执行scrapy



