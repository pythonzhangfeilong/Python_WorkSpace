from lxml import etree
from fake_useragent import UserAgent
import os
import requests
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

# http://www.kk2w1.com/

class Download_video():
    def __init__(self):
        self.url=input('请输入下载视频的url：')
        self.headers={'User-Agent':UserAgent().random}

    # 获取页面数据
    def get_url_data(self):
        try:
            response=requests.get(url=self.url,headers=self.headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                # print(res)
                print(self.url+'请求成功')
                print('等待加载页面........')
                time.sleep(3)
                return res
        except:
            return 'None'

    # 下载视频
    def download(self,res):
        html=etree.HTML(res)
        video_name=html.xpath('//*[@class="ct-c"]/dl/dt[@class="name"]/text()')[0]
        print(video_name)
        print('请求到的视频名字是:',video_name)
        video_url=html.xpath('//*[@id="vlink_1"]/ul/li/a/@href')[1]
        print('即将开始下载......')
        time.sleep(3)
        print('视频文件较大请耐心等待.......')

        os.system('you-get -o /Users/feilong/05_Code/Python_WorkSpace/8_Demo_Datas/1_Demo_Broken/Demo_Review/1_Demo_爬虫_Project/19_爬取ts结尾的视频/video %s'%video_url)

    # 启动函数
    def run(self):
        res=self.get_url_data()
        self.download(res)

if __name__ == '__main__':
    DV=Download_video()
    DV.run()




















