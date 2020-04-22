from lxml import etree
from urllib import request
import time
import re
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Pear_video():
    """请求"""
    def get_response(self,url,headers):
        try:
            response=requests.get(url=url,headers=headers)
            response.encoding=response.apparent_encoding
            res=response.text
            return res
        except:
            return ''

    """获取视频播放video_id"""
    def get_video_id(self,res):
        try:
            htnl=etree.HTML(res)
            video_id=htnl.xpath('//ul[@id="categoryList"]/li/div/a/@href')
            return video_id
        except:
            return ''

    """拼接获取到的视频id，获取视频播放地址并下载"""
    def get_video_url(self,video_id,headers):
        url='https://www.pearvideo.com/'
        for id in video_id:
            urls=url+id
            response=requests.get(url=urls,headers=headers)
            # 设置编码
            response.encoding=response.apparent_encoding
            res=response.text
            html=etree.HTML(res)
            # 匹配拼接视频名字
            video_name=html.xpath('//div[@class="details-content fix-width-center"]/div/div/h1/text()')[0]+'.mp4'
            # 获取视频的url
            video_url=re.findall(r'srcUrl="(.*?)"',res)[0]
            # 下载
            request.urlretrieve(url=video_url,filename='./video/%s'%video_name)
            print('正在下载的是:',video_name)
            time.sleep(5)

    """函数启动"""
    def run(self):
        res=self.get_response(url=url,headers=headers)
        video_id=self.get_video_id(res)
        self.get_video_url(video_id,headers)

if __name__ == '__main__':
    url='https://www.pearvideo.com/shooters'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    pear=Pear_video()
    pear.run()











