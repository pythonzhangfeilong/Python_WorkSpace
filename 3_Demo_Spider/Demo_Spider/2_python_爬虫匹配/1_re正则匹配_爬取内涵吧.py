# 1、re正则匹配
    # 正则表达式是处理字符串的强大工具，它邮资机特定的语法结构，可以实现字符串的检索、替换匹配、验证

import re                                       # 正则匹配模块
import requests                                 # 请求模块
from fake_useragent import UserAgent            # 生成浏览器模块

yuanurl='https://www.neihan-8.com/njjzw/'
headers={'User-Agent':UserAgent().random}
# 请求响应
def func_request(url):
    try:
        # 获取请求的响应
        response=requests.get(url,headers=headers)
        # 判断请求的响应是否为200（请求成功）
        if response.status_code==200:
            # 响应成功返回为二进制的内容
            return response.content.decode()
    except:
        return None
# 爬去内容匹配
def func_pq(html):
    data_list=re.findall(r'<div class="text-.*?title="(.*?)".*?<div class="desc">(.*?)</div>',html,re.S)
    # 谁调用这个函数，就返回给谁
    return data_list
# 写入文档
def func_write(data_list):
    with open('脑筋急转弯.txt','a',encoding='utf-8')as f:
        for data in data_list:
            f.write(data[0].strip()+'\t'+data[1].strip()+'\n')
if __name__ == '__main__':
    # 利用for控制下载页面
    for i in range(1,10):
        if i==1:
            url=yuanurl
            print('成功爬取',url)
        else:
            url=yuanurl+'index_'+str(i)+'.html'
        print('爬取成功',url)
        html=func_request(url)
        data_list=func_pq(html)
        func_write(data_list)





















