from bs4 import BeautifulSoup
import requests

url='http://www.netbian.com/s/wangzherongyao/'
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

response=requests.get(url=url,headers=headers)
res=response.text

soup=BeautifulSoup(res,'html.parser')

print(soup.img.attrs['src'])













