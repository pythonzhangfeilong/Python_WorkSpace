"""
@File    : 1_People_data.py
@Time    : 2020/5/12 11:31 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
from fake_useragent import UserAgent
from lxml import etree
import matplotlib
import peewee
import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

"""创建数据库表"""
class Create_database_tables():
    def __init__(self):
        self.url='https://www.hongheiku.com/sjrk/9685.html'
        self.headers={'User-Agent':UserAgent().random}

    # 创建数据库
    def create_databse(self):
        # 链接数据库
        connect=peewee.MySQLDatabase(database='02_people_datas',host='127.0.0.1',user='root',password='12345678',charset='utf8')
        # 使用cursor创建游标对象，相当于操作者
        cursor=connect.cursor()
        # 使用数据库游标对象电商execute()直接写数据库SQL语句
        cursor.execute('create table 01_spider_china_people(id int primary key auto_increment,地区 varchar(20),2019常住人口 varchar(20),2018常住人口 varchar(20),查看详细信息地址 varchar(50))')
        # 关闭游标
        cursor.close()
        # 关闭数据库
        connect.close()
        print('数据库表创建成功')

    # 请求网页数据
    def requestss_html_data(self):
        try:
            response=requests.get(url=self.url,headers=self.headers)
            if response.status_code==200:
                response.encoding=response.status_code
                res=response.text
                return res
        except:
            return 'None'

    # 匹配数据
    def matching_data(self,res):
        html=etree.HTML(res)
        items=[]
        for i in range(3,37):
            province=html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[1]/a/text()'.format(i))[0]
            people_2019=html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[2]/text()'.format(i))[0].strip()[0:-2]
            people_2018=html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[3]/text()'.format(i))[0].strip()[0:-2]
            html_data=html.xpath('/html/body/section/div[1]/div/article/table/tbody/tr[{}]/td[4]/a/@href'.format(i))[0]

            item={}
            item['diqu']=province
            item['2019_people']=people_2019
            item['2018_people']=people_2018
            item['data_html']=html_data

            items.append(item)
        return items

    # 把获取到的数据写入数据库
    def write_data(self,items_data):
        # 链接数据库
        connect = peewee.MySQLDatabase(database='02_people_datas', host='127.0.0.1', user='root', password='12345678',charset='utf8')
        # 使用cursor创建游标对象，相当于操作者
        cursor = connect.cursor()
        for item in items_data:
            sql="insert into 01_spider_china_people(地区,2019常住人口,2018常住人口,查看详细信息地址) values (%s,%s,%s,%s)"
            # 使用数据库游标对象电商execute()直接写数据库SQL语句
            cursor.execute(sql,[item['diqu'],item['2019_people'],item['2018_people'],item['data_html']])
            # 提交给数据库
            connect.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        connect.close()
        print('数据库数据写入成功')

    # 把数据库中的数据读取出来
    def read_data(self):
        # 链接数据库
        connect = peewee.MySQLDatabase(database='02_people_datas', host='127.0.0.1', user='root', password='12345678',charset='utf8')
        # 使用cursor创建游标对象，相当于操作者
        cursor = connect.cursor()
        # 使用数据库游标对象电商execute()直接写数据库SQL语句
        cursor.execute("select * from 01_spider_china_people ")
        # 查询出整张表
        data = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        connect.close()
        return data

    # 画饼状图
    def painting_pie(self,data):
        provinces=[]
        peoples_2019=[]

        for i in data:
            province=i[1]
            people_2019=i[2]
            people_2018=i[3]
            peoples_2019.append(people_2019)
            provinces.append(province)
        fraces=peoples_2019
        lables=provinces

        pyplot.rcParams['font.sans-serif'] = ['SimHei']

        pyplot.pie(x=fraces,labels=lables,autopct='%.f%%', radius=1.8)
        pyplot.show()

    def run(self):
        # 创建数据库表
        # self.create_databse()

        res=self.requestss_html_data()
        items_data=self.matching_data(res)

        # 把数据写入数据库
        # self.write_data(items_data)

        data=self.read_data()
        self.painting_pie(data)


if __name__ == '__main__':
    creates=Create_database_tables()
    creates.run()

















