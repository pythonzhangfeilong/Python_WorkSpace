from lxml import etree
import requests
import time
import pymysql
import ssl

ssl._create_default_https_context=ssl._create_unverified_context

class Fangtianxia():
    """获取页面数据"""
    def get_html_data(self):
        for i in range(1,5+1):
            url='https://nm.newhouse.fang.com/house/s/b9%d'%i
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
            response=requests.get(url=url,headers=headers)
            response.encoding='gb2312'
            time.sleep(3)
            res=response.text
            return res

    """匹配想要的数据"""
    def get_data(self):

        html_data=self.get_html_data()

        html=etree.HTML(html_data)

        title_name=html.xpath('//div[@class="nlcd_name"]/a/text()')
        name=[]
        for i_name in title_name:
            name_str=i_name.strip()
            name.append(name_str)

        title_addr=html.xpath('//div[@class="address"]/a/@title')
        addr=[]
        for i_addr in title_addr:
            addr.append(i_addr)

        money=html.xpath('//div[@class="nhouse_price"]/span/text()')

        phone=html.xpath('//div[@class="tel"]/p/text()[1]')

        return name,addr,money,phone

    """创建表"""
    def data_base(self):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db=pymysql.connect('127.0.0.1','root','12345678','fang_data',charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor=db.cursor()
        # 使用数据库游标对象，点上execute()直接写数据库sql语句
        cursor.execute("create table spider_fang(id int primary key auto_increment,name varchar(30) ,addr varchar(100),money varchar(50),phone varchar (30))")
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()

    """把数据写入数据库"""
    def xie_data(self):
        data=self.get_data()
        name=data[0]
        addr=data[1]
        money=data[2]
        phone=data[3]

        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db=pymysql.connect('127.0.0.1','root','12345678','fang_data',charset='utf8')
        # 使用cursor创建数据库游标
        cursor=db.cursor()
        # 使用游标对象点上execute编写执行sql
        insert = ("insert into spider_fang(name,addr,money,phone) values (%s,%s,%s,%s);")
        data = (name,addr,money,phone)
        cursor.execute(insert, data)
        # 提交给数据库
        db.commit()

        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()


if __name__ == '__main__':
    # 将类实例为对象
    fangtianxia=Fangtianxia()
    # 类对象调用方法
    fangtianxia.xie_data()














