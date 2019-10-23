from fake_useragent import UserAgent
from lxml import etree
from urllib import request
from urllib import parse
import requests
data_ye=int(input('请输入下载的页数：'))
for ye in range(1,data_ye+1):
    url='http://www.3dkk.com/tietu/bizhi/list_50_%d.html'%ye
    headers={'User-Agent':UserAgent().random,}

    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    res=response.text

    html=etree.HTML(res)
    # data_name=html.xpath('//div[@class="goods clearfix listbox"]/ul/li//div[@class="img"]/a/@title')
    data=html.xpath('//div[@class="goods clearfix listbox"]/ul/li//div[@class="img"]/a/img/@src')
    print('第%d页'%ye,'共获取到%d张图片'%len(data))

    for img_url in data:
        img_name=img_url.split()[0][-15:]
        print('正在下载的是：',img_name)
        request.urlretrieve(url=img_url,filename='./images/%s'%img_name)

    print('第%d页'%ye,'%d张图片下载完成了'%len(data))



