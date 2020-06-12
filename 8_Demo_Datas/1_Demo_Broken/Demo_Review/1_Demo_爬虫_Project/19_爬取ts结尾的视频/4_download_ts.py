"""
@File    : 4_download_ts.py
@Time    : 2020/6/3 11:18 上午
@Author  : FeiLong
@Software: PyCharm
"""
from fake_useragent import UserAgent
from urllib import request
import requests
import threading,time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


lock = threading.Lock()
class Download_ts():
    def create_ts(self):
        url = 'https://www.mantoubo3.com/videos/202003/5e6cb100144a59081f203a8a/6g62a8/index.m3u8'
        headers={'User-Agent':UserAgent().random}
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        data_res = response.text
        ts_list = data_res.split()[5:][::2]
        for i in ts_list:
            data = 'https://www.mantoubo3.com/videos/202003/5e6cb100144a59081f203a8a/6g62a8/' + i
            print('即将下载' + data)
            request.urlretrieve(url=data, filename='./videoss/{}'.format(i))
            print('下载完成' + data)

if __name__ == '__main__':

    # 获取主线程的名字
    print('主线程开始:', threading.current_thread().name)
    list_null = []
    '''
    下面利用for循环的便利次数，得到了对应个数的线程，然后把创建好的一个个线程加入到空列表中
    '''
    for i in range(20):
        # 创建一个线程
        t = threading.Thread(target=Download_ts.create_ts,*self)
        list_null.append(t)
    # 所有的线程放在列表中统一的执行
    for t in list_null:
        t.start()
    print('主线程结束:', threading.current_thread().name)