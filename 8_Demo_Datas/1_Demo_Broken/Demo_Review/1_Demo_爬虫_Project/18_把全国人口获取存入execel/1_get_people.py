"""
@File    : 1_get_people.py
@Time    : 2020/4/20 3:34 下午
@Author  : FeiLong
@Software: PyCharm
"""
from fake_useragent import UserAgent
from lxml import etree
from bs4 import BeautifulSoup
from matplotlib import pyplot
from matplotlib.ticker import MultipleLocator,FormatStrFormatter
import numpy
import matplotlib
import requests
import xlwt
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


class People():
    def __init__(self):
        self.url='https://www.hongheiku.com/sjrk/9685.html'
        self.headers = {'User-Agent': UserAgent().random}

    def get_html(self):
        try:
            response=requests.get(url=self.url,headers=self.headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                return res
        except:
            return 'None'

    def get_data_province(self,res):

        Soup=BeautifulSoup(res,'lxml')
        data=Soup.select('.article-content table tr')

        # X轴的数据
        province=[]

        for i in data:
            sheng=i.select('td')[0].get_text()
            province.append(sheng)
        return province

    def get_data_peoples(self,res):
        html=etree.HTML(res)
        peoples=[]

        for i in range(2,37):
            people=html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[2]/text()'.format(i))[0]
            peoples.append(people)
        return peoples

    def get_data_peopless(self,res):
        html = etree.HTML(res)
        peopless = []

        for i in range(2, 37):
            people = html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[3]/text()'.format(i))[0]
            peopless.append(people)
        return peopless

    def get_data_html(self,res):
        html = etree.HTML(res)
        htmls = []

        for i in range(2, 37):
            html_d = html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[4]/a/@href'.format(i))[0]
            htmls.append(html_d)
        return htmls

    def write_data_execle(self):
        res = self.get_html()
        province =self.get_data_province(res)
        peoples =self.get_data_peoples(res)
        peopless=self.get_data_peopless(res)
        htmls=self.get_data_html(res)

        book=xlwt.Workbook(encoding='UTF-8')
        sheet = book.add_sheet('全国各省人口')
        sheet.write(0,1,'2019年常住人口')
        sheet.write(0,2,'2018年常住人口')
        sheet.write(0, 3, '详细信息')

        i=0
        for data_province in province:
            sheet.write(i,0,data_province)
            i+=1
        s=1
        for data_peoples in peoples:
            sheet.write(s,1,data_peoples)
            s+=1
        y=2
        for data_people in peopless:
            sheet.write(y, 2, data_people)
            y += 1
        z=3
        for html in htmls:
            sheet.write(z,3,html)
            z+=1
        book.save('./各省人口.xls')


    def run(self):
        self.write_data_execle()

if __name__ == '__main__':
    people=People()
    people.run()
















