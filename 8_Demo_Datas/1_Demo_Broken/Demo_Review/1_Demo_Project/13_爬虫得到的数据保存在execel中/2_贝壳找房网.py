from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import xlwt
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class BeiKe():
    """获取页面数据"""
    def get_html(self,url,headers):
        try:
            response = requests.get(url=url, headers=headers)
            if response.status_code==200:
                response.encoding = response.apparent_encoding
                res = response.text
                return res
        except:
            return ''

    """获取需要的数据"""
    def get_data(self,res_data):
        soup=BeautifulSoup(res_data,'lxml')
        data_list=soup.select('.info')
        items=[]
        for data in data_list:
            item={}
            house_html=data.select('.title a')[0].get('href')
            house_title=data.select('.title a')[0].get_text()
            house_addr=data.select('.positionInfo a')[0].get_text()
            house_type=data.select('.houseInfo')[0].get_text().replace('|',' ').strip().split()
            house_time=data.select('.followInfo')[0].get_text().replace('/',' ').strip().split()
            house_money_zong=data.select('.totalPrice span')[0].get_text().replace('元/平米',' ')
            house_money_dan=data.select('.unitPrice span')[0].get_text().replace('单价',' ')

            item['小区url']=house_html
            item['小区介绍']=house_title
            item['小区地址']=house_addr
            item['房屋类型']=house_type
            item['小区发布时间']=house_time
            item['房子总价']=house_money_zong
            item['房子每平米单价']=house_money_dan

            items.append(item)
        return items

    """写入execel"""
    def write_execel(self,items):
        book = xlwt.Workbook(encoding='utf-8')
        sheet = book.add_sheet('呼和浩特市二手房')
        sheet.write(0,0,'房子查看html')
        sheet.write(0, 1, '房子介绍')
        sheet.write(0, 2, '小区所在地址')
        sheet.write(0, 3, '房子类型')
        sheet.write(0, 4, '房子信息关注人数和时间')
        sheet.write(0, 5, '房子总价(单位：万元)')
        sheet.write(0, 6, '房子每平米单价(单位：元/平米)')
        i = 1
        for imgs in items:
            sheet.write(i, 0, imgs['小区url'])
            sheet.write(i, 1, imgs['小区介绍'])
            sheet.write(i, 2, imgs['小区地址'])
            sheet.write(i, 3, imgs['房屋类型'])
            sheet.write(i, 4, imgs['小区发布时间'])
            sheet.write(i, 5, imgs['房子总价'])
            sheet.write(i, 6, imgs['房子每平米单价'])
            # 每写完一行数据，下一次换到下一行
            i += 1
        book.save('./贝壳_呼和浩特市二手房数据.xls')
        print('本次数据写入完成')

    """启动函数"""
    def run(self):
        res_data=self.get_html(url=url,headers=headers)
        items=self.get_data(res_data)
        self.write_execel(items)

if __name__ == '__main__':
    url = 'https://hhht.ke.com/ershoufang/'
    headers = {'User-Agent': UserAgent().random}
    beike=BeiKe()
    beike.run()






