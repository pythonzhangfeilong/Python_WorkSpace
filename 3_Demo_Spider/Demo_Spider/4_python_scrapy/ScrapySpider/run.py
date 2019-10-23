# 导入scrapy执行命令的接口
from scrapy import cmdline
# 调用接口执行命
#####注意：执行文件的名字并不是文件的名字，而是编写SpidrTest时里面这是的name
# cmdline.execute("scrapy crawl baiduSpider".split())

# 重构之后的执行
cmdline.execute('scrapy crawl baiduSpider_chonggou'.split())




























