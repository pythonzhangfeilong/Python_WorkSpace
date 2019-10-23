from urllib import request
from fake_useragent import UserAgent
from lxml import etree

# 请输入爬去的页数
ye_data=int(input('请输入爬取得页数：'))
for i in range(ye_data):
    i_data=i+1
    url='http://jandan.net/pic/page-%d#comments'%i_data

    print('正在下载的url是：',url)

    headers={'User-Agent':UserAgent().random}

    req=request.Request(url=url,headers=headers)

    response=request.urlopen(req)

    res=response.read().decode('utf-8')

    html=etree.HTML(res)

    link=html.xpath("//div[@class='text']/p/a/@href")

    for i in link:
        http_url='http:'+i
        img_name=i.rsplit()[0][-10:]
        print('%s 正在下载'%img_name)
        request.urlretrieve(url=http_url,filename='./image/%s'%img_name)
    print('完成下载的url是：',url)









