# 导入cmd执行命令模块
from scrapy import cmdline
# 编写cmd执行语句，crawl后面跟的是根目录下，爬虫文件代码中自己定义的名字
cmdline.execute('scrapy crawl baidu'.split())













