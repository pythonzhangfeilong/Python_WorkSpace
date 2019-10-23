import requests
from fake_useragent import UserAgent

url='https://www.baidu.com/s?'

headers={'User-Agent':UserAgent().random}

neirong=input('请输入搜索的关键字:')

data={'wd':neirong}

proxy={'http':'http://219.159.38.197:56210'}

response=requests.get(url=url,headers=headers,params=data,proxies=proxy)

print(response.text)
















