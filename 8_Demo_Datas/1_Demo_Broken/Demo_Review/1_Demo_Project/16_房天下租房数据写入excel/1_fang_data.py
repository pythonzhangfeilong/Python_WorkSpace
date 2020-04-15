"""
@File    : 1_fang_data.py
@Time    : 2020/4/8 9:44 上午
@Author  : FeiLong
@Software: PyCharm
"""
from bs4 import BeautifulSoup
import requests
import xlwt

class Fang_data():
    """获取页面数据"""
    def get_html(self,url):
        try:
            response=requests.get(url)
            if  response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                print(url,'数据获取成功')
                return res
        except:
            return ''

    """获取需要的数据"""
    def get_data(self,res):
        soup=BeautifulSoup(res,'lxml')
        data_list=soup.select('.list')
        items=[]
        for data in data_list:
            item={}
            house_html='https://nm.zu.fang.com/'+data.select('.title a ')[0].get('href')
            house_title=data.select('.title a')[0].get('title')
            house_xinxi=data.select('.font15')[0].get_text().replace('|','').strip().split()
            house_addr=data.select('.gray6')[0].get_text()
            house_monney=data.select('.mt5')[0].get_text()

            item['小区url'] = house_html
            item['小区介绍'] = house_title
            item['小区信息'] = house_xinxi
            item['小区地址'] = house_addr
            item['房租价钱'] = house_monney
            items.append(item)
        return items

    """写入excel"""
    def write_execel(self,items):
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('呼和浩特市房屋出租信息')
        sheet.write(0,0,'查看房子的url')
        sheet.write(0,1,'房子介绍')
        sheet.write(0,2,'小区信息')
        sheet.write(0,3,'小区地址')
        sheet.write(0,4,'房租价钱')
        i=1
        for imgs in items:
            sheet.write(i, 0, imgs['小区url'])
            sheet.write(i, 1, imgs['小区介绍'])
            sheet.write(i, 2, imgs['小区信息'])
            sheet.write(i, 3, imgs['小区地址'])
            sheet.write(i, 4, imgs['房租价钱'])
            i += 1
        book.save('./呼和浩特市租房数据.xls')
        print(url,'本次数据写入完成')


    """启动函数"""
    def run(self):
        res=self.get_html(url)
        items=self.get_data(res)
        self.write_execel(items)


if __name__ == '__main__':
    url='https://nm.zu.fang.com'
    # headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    fang_data=Fang_data()
    fang_data.run()