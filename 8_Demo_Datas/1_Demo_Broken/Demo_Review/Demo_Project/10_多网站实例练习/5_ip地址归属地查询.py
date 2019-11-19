from lxml import etree
import requests
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url='http://m.ip138.com/ip.asp?ip='
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

ip_input=input('请输入查询的IP地址：')
urls='http://m.ip138.com/ip.asp?ip=%s'%ip_input

response=requests.get(url=urls,headers=headers)

time.sleep(2)
if response.status_code==200:
    print('%s查询访问成功'%ip_input)
else:
    print('%s查询访问失败'%ip_input)

response.encoding='utf-8'
res=response.text

html=etree.HTML(res.encode('utf-8'))

html_data=html.xpath('//div[@class="module"]/p[@class="result"]/text()')

print('正在查询请稍后')

time.sleep(3)

for i in html_data:
    print(i)






