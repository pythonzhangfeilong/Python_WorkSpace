from lxml import etree
from bs4 import BeautifulSoup
import requests
import pymysql
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Anjuke():
    """获取网页数据"""
    def get_html(self,url,headers):
        try:
            response=requests.get(url=url,headers=headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                return res
        except:
            return ''

    """获取想要的数据"""
    def get_data(self,res_data):
        soup=BeautifulSoup(res_data,'lxml')
        building_list=soup.select('.infos')
        items=[]
        for i in building_list:
            item={}
            building_name=i.select('.items-name')[0].get_text()
            building_addr=i.select('.list-map')[0].get_text()
            building_huxing=i.select('.huxing')[0].get_text().strip().split()
            building_data=i.select('.tag-panel')[0].get_text()

            item['楼盘名字']=building_name
            item['楼盘地址'] = building_addr
            item['楼盘户型'] = building_huxing
            item['楼盘其他信息'] = building_data

            items.append(item)

            # building_money=soup.select('.favor-pos').get_text().strip().split()
            # item['楼盘售价'] = building_money
            #
            # items.append(item)
        print(items)


    """创建数据库表"""
    def create_table(self):
        pass

    """写入数据库"""
    def write_data(self):
        pass

    """启动函数"""
    def run(self):
        res_data=self.get_html(url=url,headers=headers)
        self.get_data(res_data)

if __name__ == '__main__':
    url='https://hhht.fang.anjuke.com/?from=navigation'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    anjuke=Anjuke()
    anjuke.run()















