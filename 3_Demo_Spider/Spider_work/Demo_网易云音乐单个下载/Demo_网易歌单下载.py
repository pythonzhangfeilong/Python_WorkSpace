import requests
import re
from multiprocessing import Pool
from fake_useragent import UserAgent

# 随机产生浏览器
headers={'user-agent':UserAgent().random}
#获取每个歌单的id
def get_page(url):
    # 获取请求
    res=requests.get(url,headers=headers)
    # 正则匹配
    data=re.findall('<a title="(.*?)" href="/playlist\?id=(\d+)" class="msk"></a>', res.text)
    print(data)
    # 创建线程池
    pool = Pool(processes=4)
    pool.map(get_songs, data)
    print("下载完毕！")
def get_songs(data):
    # 拼接url地址
    playlist_url = "https://music.163.com/playlist?id=%s" % data[1]
    print(playlist_url)
    # 获取请求
    res = requests.get(playlist_url, headers=headers)
    # 正则匹配
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        print(download_url)
        # 打开一个文件，将数据写入
        try:
            with open('./music/' + i[1]+'.mp3', 'wb') as f:
                f.write(requests.get(download_url, headers=headers).content)
        except FileNotFoundError:
            pass
        except OSError:
            pass
if __name__ == '__main__':
    # 个单地址
    hot_url = "https://music.163.com/discover/playlist/?order=hot"
    # 调用封装的函数传入地址
    get_page(hot_url)




















