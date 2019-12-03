import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import xlwt
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url='http://www.netbian.com/s/huyan/'
headers={'Usr-Agent':UserAgent().random}

response=requests.get(url=url,headers=headers)

response.encoding=response.apparent_encoding

res=response.text

soup=BeautifulSoup(res,'lxml')

data_lists=soup.select('.list')

items=[]
for i in data_lists:
    item={}
    img_name = i.select('img')[0].get('alt')
    img_url=i.select('img')[0].get('src')

    item['img_name'] = img_name
    item['img_url'] = img_url
    items.append(item)

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('图片data_1')
sheet.write(0, 0, '图片名字')
sheet.write(0, 1, '图片地址')
i = 1
for imgs in items:
    #写入图片名字
    sheet.write(i, 0, imgs['img_name'])
    #写入图片地址
    sheet.write(i,1,imgs['img_url'])
    #每写完一行数据，下一次换到下一行
    i += 1
book.save('./img.xls')

















