from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib import parse
import json
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
"""身份证校验"""
class ID_card_inspection():
    """构造url和请求头"""
    def create_url_headers(self):
        id_input=int(input('请输入查询的身份证号：'))
        sourse={'id':id_input}
        urls=parse.urlencode(sourse)
        url = 'https://shenfen.supfree.net/search.asp?'+urls
        return url

    """发起请求，获取页面数据"""
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
        data_list=soup.select('.ctable')
        items=[]
        for i in data_list:
            item={}
            select_id=i.select('td')[1].get_text()
            select_addr=i.select('td')[3].get_text()
            select_birth_time=i.select('td')[5].get_text().replace('(生日配对 生日密码 历史上的今天)',' ')
            select_gender=i.select('td')[7].get_text()
            select_hefa=i.select('td')[9].get_text()

            item['查询的身份证号是'] = select_id
            item['身份证所在地'] = select_addr
            item['出生日期'] = select_birth_time
            item['性别'] = select_gender
            item['身份证号码合法性'] = select_hefa

            items.append(item)
        return items

    """写入json文件"""
    def write_json(self,items):
        json.dump(items,open('./身份证查询.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)
        print('数据写入成功')

    """启动函数"""
    def run(self):
        url=self.create_url_headers()
        res_data=self.get_html(url=url,headers=headers)
        items=self.get_data(res_data)
        self.write_json(items)

if __name__ == '__main__':
    headers = {"User-Agent": UserAgent().random}
    id=ID_card_inspection()
    id.run()





















