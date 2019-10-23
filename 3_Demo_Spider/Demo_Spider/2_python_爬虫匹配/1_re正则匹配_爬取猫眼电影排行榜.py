import csv
import re
import requests
from fake_useragent import UserAgent
# 原有链接
yuan_url='https://maoyan.com/board/4'
# 点击页数的链接
yeshu_url='https://maoyan.com/board/4?offset=10'
# 随机产生浏览器
headers={'User-Agent':UserAgent().random}
# 请求
def func_request(yuan_url):
    try:
        # 获取请求响应
        response=requests.get(yuan_url,headers)
        # 判断请求响应是否成功
        if response.status_code==200:
            # 响应成功返回为字节型式的内容
            return response.content.decode()
    except:
        return None
# 匹配内容
def func_re(html):
    data_list=re.findall(r'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',html,re.S)
    # 谁调用这个函数，返回给谁
    return data_list
# 写入到csv中
def func_write(datas):
    with open('maoyan.csv','a',newline='')as f:
        writer=csv.writer(f)
        writer.writerow(["电影名称", "主演", "上映时间"])
        for data in datas:
            # 创建写入对象
            writer = csv.writer(f)
            L = [data[0].strip(), data[1].strip(), data[2].strip()]
            writer.writerow(L)
def main(offset):
    url = 'https://maoyan.com/board/4?offset={}'.format(offset)
    html = func_request(url)
    data = func_re(html)
    func_write(data)
if __name__ == '__main__':
    for i in range(0,10):
        main(str(i*10))








