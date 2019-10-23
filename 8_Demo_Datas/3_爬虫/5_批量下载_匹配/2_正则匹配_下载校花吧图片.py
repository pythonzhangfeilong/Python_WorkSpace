from urllib import request
from fake_useragent import UserAgent
import re

# 请求的url
url='http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1'

# 生成随机的请求头
headers={'User-Agent':UserAgent().random}

# 创建请求
req=request.Request(url=url,headers=headers)

# 进行请求
response=request.urlopen(req)

# 读取请求到的内容
html=response.read().decode('utf-8')

# 匹配图片的url
img_url=re.findall(r'<img .*? bpic="(.*?)"',html)

# 遍历url列表
for i in img_url:
    # 截取末尾的字符串作为图片的名字
    img_name=i.rsplit()[0][-15:]
    # 请求图片的地址并且保存在本地
    request.urlretrieve(url=i,filename='./image/%s'%img_name)