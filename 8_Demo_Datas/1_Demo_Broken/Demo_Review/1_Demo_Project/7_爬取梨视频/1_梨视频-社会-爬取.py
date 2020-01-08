from urllib import request
from lxml import etree
import re
import selenium
from selenium import webdriver
import time
import ssl

# 取消本地证书验证
ssl._create_default_https_context = ssl._create_unverified_context
# 梨视频社会类地址
url='https://www.pearvideo.com/category_1'
# 复制的浏览器请求头
headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

###### 使用selenium爬取多页
# driver=webdriver.Chrome()
# # 请求指定的url
# driver.get(url=url)
# for i in range(1,5+1):
#     # 执行js代码
#     time.sleep(2)
#     # 模拟滚动浏览器右侧的滚动条，滚动到底部，用来增加页数
#     driver.execute_script('scrollTo(0,document.body.scrollHeight)')
# time.sleep(3)
# driver.quit()
###### 使用selenium爬取多页


# 构建请求内容
req=request.Request(url=url,headers=headers)
# 获取请求到的内容
response=request.urlopen(req)
# 读取请求的全部信息
res=response.read().decode('utf-8')
# 将获取的内容格式化为可以操作的对象
html=etree.HTML(res)
# 使用xpath获取播放视频跳转的html地址
htmls=html.xpath('//*[@id="categoryList"]/li/div/a/@href')
# xpath匹配出的播放视频跳转的html地址是一个列表，进行遍历
for var in htmls:
    li_video='https://www.pearvideo.com/'
    # 看视频跳转页的url
    video_html=li_video+var
    # 复制的浏览器请求头
    headers_html={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    # 构建请求
    video_req=request.Request(url=video_html,headers=headers_html)
    # 获取请求到的内容
    video_response=request.urlopen(video_req)
    # 读取请求的全部内容
    video_res=video_response.read().decode('utf-8')
    # 将获取到的内容转换为可操作的对象
    video_html_htmls=etree.HTML(video_res)
    # xpath匹配获取视频标题
    video_name=video_html_htmls.xpath('//*[@id="detailsbd"]//h1/text()')
    # 正则匹配获取视频播放的url
    video_urls=re.findall(r'srcUrl="(.*?)"',video_res)
    # 遍历去除列表符号
    for ii in video_urls:
        video_urlss=ii
        for i in video_name:
            # 创建拼接视频名字
            video_names=i+'.mp4'
            print('正在下载的是:',video_names)
            # 下载视频
            request.urlretrieve(url=video_urlss,filename='./video/%s'%video_names)
            time.sleep(2)






























