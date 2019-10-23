# scrapy执行命令的接口
from scrapy import cmdline
# 调用执行命令
cmdline.execute('scrapy crawl images'.split())