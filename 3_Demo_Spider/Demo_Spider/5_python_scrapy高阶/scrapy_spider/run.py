# 导入cmd执行模块
# from scrapy import cmdline
# get请求
# 编写cmd执行语句
# cmdline.execute('scapry crawl baidu'.split())

# 导入cmd执行模块
# from scrapy import cmdline
# # xpath
# # 编写cmd执行语句
# cmdline.execute('scrapy crawl baidu_Xpath'.split())

# 导入cmd执行模块
# from scrapy import cmdline
# # css
# # 编写cmd执行语句
# cmdline.execute('scrapy crawl baidu_css'.split())

# 导入cmd执行模块(匹配不出来)
# from scrapy import cmdline
# # re
# cmdline.execute('scrapy crawl gif_re'.split())

# 导入cmd执行模块
from scrapy import cmdline
# extract
cmdline.execute('scrapy crawl baidu_Extract'.split())













