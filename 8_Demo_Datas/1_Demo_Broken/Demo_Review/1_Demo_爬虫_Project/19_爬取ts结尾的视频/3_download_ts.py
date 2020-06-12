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

    def create_ts(self):
        url='https://www.mantoubo3.com/videos/202003/10/5e675386144a59081f202f77/b5a495/index.m3u8'
        response = requests.get(url=url, headers=self.headers)
        response.encoding = response.apparent_encoding
        data_res = response.text
        ts_list=data_res.split()[5:][::2]
        return ts_list

    def download_ts(self,ts_list):
        print(len(ts_list))
        for i in ts_list:
            data='https://www.mantoubo3.com/videos/202003/10/5e675386144a59081f202f77/b5a495/'+i
            print('即将下载'+data)
            request.urlretrieve(url=data,filename='./videos/{}'.format(i))
            print('下载完成'+data)

    def run(self):
        ts_list=self.create_ts()
        self.download_ts(ts_list)

if __name__ == '__main__':
    downloads_ts=Download_ts()
    downloads_ts.run()
