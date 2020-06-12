"""
@File    : 2_download_ts.py
@Time    : 2020/6/2 11:53 上午
@Author  : FeiLong
@Software: PyCharm
"""
from fake_useragent import UserAgent
from lxml import etree
from urllib import request
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Download_ts():

    def __init__(self):
        self.url='http://www.kk2w1.com/'
        self.headers={'User-Agent':UserAgent().random}
    #
    # def get_html(self):
    #     try:
    #         response=requests.get(url=self.url,headers=self.headers)
    #         if response.status_code==200:
    #             response.encoding=response.apparent_encoding
    #             res=response.text
    #             print(res)
    #             return res
    #     except:
    #         return 'None'
    #
    # def get_data(self,res):
    #     html=etree.HTML(res)
    #     video_url='http://www.kk2w1.com/'+html.xpath('//*[@id="tv-directory"]/ul/div/div[1]/div[1]/ul/li[1]/a/@href')[0]
    #     response=requests.get(url=video_url,headers=self.headers)
    #     response.encoding = response.apparent_encoding
    #     data_res = response.text
    #     html=etree.HTML(data_res)
    #     videos_url='http://www.kk2w1.com/'+html.xpath('//*[@id="vlink_1"]/ul/li/a/@href')[0]
    #     print(videos_url)

    def create_ts(self):
        url='https://www.mantoubo3.com/videos/202003/5e6cb100144a59081f203a8a/6g62a8/index.m3u8'
        response = requests.get(url=url, headers=self.headers)
        response.encoding = response.apparent_encoding
        data_res = response.text
        ts_list=data_res.split()[5:][::2]
        return ts_list

    def download_ts(self,ts_list):
        print(len(ts_list))
        for i in ts_list:
            data='https://www.mantoubo3.com/videos/202003/5e6cb100144a59081f203a8a/6g62a8/'+i
            print('即将下载'+data)
            request.urlretrieve(url=data,filename='./video/{}'.format(i))
            print('下载完成'+data)

            # start = datetime.datetime.now().replace(microsecond=0)
            # end = datetime.datetime.now().replace(microsecond=0)
            # print("耗时：%s" % (end - start))

    def run(self):
        # res=self.get_html()
        # self.get_data(res)

        ts_list=self.create_ts()
        self.download_ts(ts_list)

if __name__ == '__main__':
    downloads_ts=Download_ts()
    downloads_ts.run()
