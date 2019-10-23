from bs4 import BeautifulSoup
import requests
import re,time
from fake_useragent import UserAgent
# 准备的url地址
url="http://www.budejie.com/video/"
# 爬取函数
def get_page(url,data=None):
    # 随机的生成一个浏览器
    header={'User-Agent': UserAgent().random}
    # 请求响应的信息
    html = requests.get(url,headers=header)

    soup=BeautifulSoup(html.text,"html.parser")

    lists = soup.findAll('a',href=re.compile('http://svideo.spriteapp.com/video/2019/(.*?).mp4'))
    # print(lists)
    a = 0
    for i in lists:
        a+=1
        url_href = i.get("href")
        print(url_href)
        req= requests.get(url_href)
        # print("num"+str(a)+"video")
        with open(str(time.time())+".mp4","wb") as file:
            file.write(req.content)
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)
if __name__ == '__main__':
    get_more_pages(1,2)
