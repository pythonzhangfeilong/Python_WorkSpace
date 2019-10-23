# 导入cmd执行模块
from scrapy import cmdline
# 编写执行语句,crawl后面跟的是爬虫根目录下文件代码中的名字
cmdline.execute('scrapy crawl baidu'.split())