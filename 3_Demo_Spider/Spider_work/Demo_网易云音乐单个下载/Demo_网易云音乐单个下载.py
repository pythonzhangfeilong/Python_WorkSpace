import re
import urllib.request
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

#获取响应
def getResponse(url,headers):
    try:
        # 模拟浏览器获取请求
        response=requests.get(url,headers=headers)
        #如果响应成功，就返回响应
        if response.status_code==200:
            return response
        return None
    except RequestException as e:
        return None

def getSongName(songid):
    #随机产生一个浏览器
    headers={'user-agent':UserAgent().random}
    url='https://music.163.com/song?id={}'.format(songid)
    # 获取文本
    text=getResponse(url,headers).text
    # 正则匹配
    # title=re.findall('<title>(.*?)</title>',text,re.S)
    # 美丽汤匹配
    soup=BeautifulSoup(text,'lxml')
    title=soup.title.text
    # 获取歌名
    name=title.split('-')[0]
    return  name.strip()

if __name__ == '__main__':
    songid=input('请输入你要下载歌曲的id：')
    # 下载歌曲的url,外部提供
    url='http://music.163.com/song/media/outer/url?id={}'.format(songid)
    # 请求头
    headers={'user-agent':UserAgent().random}
    #下载
    down_url=getResponse(url,headers).url
    SongName=getSongName(songid)
    #最终的下载到本地
    urllib.request.urlretrieve(down_url,'./music/'+SongName+'.mp3')

















