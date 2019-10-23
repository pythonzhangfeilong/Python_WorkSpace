# 导入scrapy执行命令的接口
from scrapy import cmdline
# 调用命令接口执行
# cmdline.execute('scrapy crawl images'.split())

# 把图片的地址存在一个csv文件中方便调用
cmdline.execute('scrapy crawl images -o images.csv'.split())

# 把图片的地址存在一个json中
# cmdline.execute('scrapy crawl images -o images.json'.split())