from urllib import request
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

# 处理url
def func_ye(url,headers):
    s_url=int(input('请输入要爬取得页数：'))
    for i in range(1,s_url+1):
        full_url=url%i
        print('爬取得url是：',full_url)
        func_parse(full_url,headers)

# 获取页面数据
def func_parse(url,headers):
    '''
    :param url: 请求地址
    :param headers: 请求头
    :return: None
    '''
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    res = response.read().decode('utf-8')
    soup = BeautifulSoup(res, 'lxml')
    house_list = soup.select('.house-details')
    items = []

    for house_data in house_list:
        title = house_data.select('.house-title a')[0].get_text()
        data = house_data.select('.details-item')[0].get_text()
        address = house_data.select('.comm-address')[0].get_text()
        item = {}
        item['title'] = title
        item['data'] = data
        item['address'] = address

        items.append(item)

    json.dump(items, open('anjuke.json', 'a', encoding='utf-8'), ensure_ascii=False, indent=4)

if __name__ == '__main__':
    url='https://huhehaote.anjuke.com/sale/saihan/p%s/'
    headers={'User-Agent':UserAgent().random}
    func_ye(url,headers)

