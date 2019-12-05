from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def func_spider():
    url = 'https://hhht.fang.lianjia.com/loupan/'
    headers = {'User-Agent': UserAgent().random}
    response = requests.get(url=url, headers=headers)
    res = response.text
    soup = BeautifulSoup(res, 'lxml')
    data_list = soup.select('.resblock-list')

    items=[]
    for data in data_list:
        item = {}
        house_title = data.select('.resblock-name a')[0].get_text()
        house_type = data.select('.resblock-name span')[0].get_text()
        house_xiaoshou = data.select('.sale-status ')[0].get_text()
        house_addr_qu = data.select('.resblock-location span')[0].get_text()
        house_addr_shangquan = data.select('.resblock-location span')[1].get_text()
        house_addr_xiangxi = data.select('.resblock-location a')[0].get_text()
        house_fangshi_type = data.select('.resblock-room')[0].get_text().strip().replace('/', '').split()
        house_pingmi = data.select('.resblock-area span')[0].get_text()
        house_maidian = data.select('.resblock-tag')[0].get_text().split()
        house_danjia = data.select('.main-price span')[0].get_text() + '元/平米'
        house_money = data.select('.resblock-price')[0].get_text().split()

        item['house_title'] = house_title
        item['house_type'] = house_type
        item['house_xiaoshou'] = house_xiaoshou
        item['house_addr_qu'] = house_addr_qu
        item['house_addr_shangquan'] = house_addr_shangquan
        item['house_addr_xiangxi'] = house_addr_xiangxi
        item['house_fangshi_type'] = house_fangshi_type
        item['house_pingmi'] = house_pingmi
        item['house_maidian'] = house_maidian
        item['house_danjia'] = house_danjia
        item['house_money'] = house_money

        items.append(item)
    return render_template('链家.html',items=items)



if __name__ == '__main__':
# Flask类的run()方法在本地开发服务器上运行应用程序
    app.run()