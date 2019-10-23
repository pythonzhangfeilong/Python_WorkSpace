import requests
from fake_useragent import UserAgent
import re
# 爬取的url
base_url='https://www.neihan8.com/njjzw/'
# 随机产生一个浏览器
headers={'User-Agent':UserAgent().random}

def load_page(url):
    try:
        # 获取请求状态
        response=requests.get(url,headers=headers)

        # 判断请求状态是否为200
        if response.status_code==200:
            # 返回页面字节流
            return response.content.decode()
    except:
        return None
# 匹配
def parse_page(html):
    # 匹配的标签，把想要的内容变成.*?
    data_list = re.findall(r'<div class="text-.*?title="(.*?)".*?<div class="desc">(.*?)</div>',html,re.S)
    return data_list

# 把读取到的数据写入文件中
def write_page(data_list):
    with open('脑筋急转弯.txt','a',encoding='utf-8')as f:
        for data in data_list:
            f.write(data[0].strip()+'\t'+data[1].strip()+'\n')
            # f.write(data[1].strip()+'\n')
            f.write('\n')
if __name__ == '__main__':
    for i in range(1,10):
        if i == 1:
            url = base_url
        else:
            url = base_url+'index_'+str(i)+'.html'
        print(url)
        html = load_page(url)
        data_list = parse_page(html)
        write_page(data_list)
