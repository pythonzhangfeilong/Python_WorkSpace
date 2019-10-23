from selenium import webdriver
from urllib import request
import time
from lxml import etree

path = r'D:\Program Files\Chrome\WebDirver\chromedriver.exe'
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B1%DA%D6%BD&fr=ala&ala=1&pos=0&alatpl=wallpaper&oriquery=%E5%A3%81%E7%BA%B8'

# 创建驱动对象
driver = webdriver.Chrome(path)
# 访问指定的url
driver.get(url=url)
for i in range(5):
    # 执行js代码
    time.sleep(2)
    # 模拟滚动浏览器右侧的滚动条，滚动到底部，用来增加页数
    driver.execute_script('scrollTo(0,document.body.scrollHeight)')
time.sleep(3)

# 获取页面源码
html = driver.page_source
# 解析页面源码为lxml格式
htmls = etree.HTML(html)
# 匹配获取url
link_list = htmls.xpath('//ul[starts-with(@class,"imglist")]/li/@data-objurl')
print('共获取到%d条数据' % len(link_list))


for ii in link_list:
    img_name = ii.rsplit()[0][-15:]
    print('正在下载的是：', img_name)
    request.urlretrieve(url=ii, filename='./images/%s' % img_name)
driver.quit()











