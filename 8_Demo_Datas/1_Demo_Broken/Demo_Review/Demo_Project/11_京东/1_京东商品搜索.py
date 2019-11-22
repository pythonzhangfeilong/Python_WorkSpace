from bs4 import BeautifulSoup
import pymysql
import requests
import json
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Jingdong():
    """获取页面数据"""
    def html_data(self,url,headers):
        try:
            response=requests.get(url=url,headers=headers)
            if response.status_code==200:
                response.encoding=response.apparent_encoding
                res=response.text
                print(url,'请求成功并且获取到数据')
                return res
        except:
            return ''

    """匹配想要的数据"""
    def get_data(self,res_data):
        soup=BeautifulSoup(res_data,'lxml')
        commodity_list=soup.select('.gl-i-wrap')
        items=[]
        for commodity in commodity_list:
            img_url=commodity.select('.p-img img')[0].get('source-data-lazy-img')
            money=commodity.select('.p-price strong')[0].get_text()
            commodity_address=commodity.select('.p-name a')[0].get('href')
            phone_data=commodity.select('.p-name em')[0].get_text()
            phone_discount_data=commodity.select('.p-name i')[0].get_text()
            commodity_data=commodity.select('.p-icons')[0].get_text().strip()
            item={}
            item['商品图片地址'] = img_url
            item['商品价格'] = money
            item['商品地址'] = commodity_address
            item['商品配置'] = phone_data
            item['商品优惠'] = phone_discount_data
            item['商品其他数据'] = commodity_data

            items.append(item)
        return items

    """写入json文件"""
    def write_json(self,items):
        json.dump(items,open('jingdong.json','a',encoding='utf-8'),ensure_ascii=False,indent=4)

    """创建数据库表"""
    def create_table(self):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db = pymysql.connect('127.0.0.1', 'root', '12345678', '01_spider_data', charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor = db.cursor()
        # 使用数据库游标对象，点上execute()直接写数据库sql语句
        cursor.execute("create table 01_spider_jingdong(id int primary key auto_increment,商品图片地址 varchar(1000) ,商品价格 varchar(1000),商品地址 varchar(2000),商品配置 varchar (1000),商品优惠 varchar (1000),商品其他数据 varchar (1000))")
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('数据库表创建成功')

    """把数据写入数据库"""

    def write_data(self, items):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db = pymysql.connect('127.0.0.1', 'root', '12345678', '01_spider_data', charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor = db.cursor()
        for item in items:
            # 使用数据库游标对象，点上execute()直接写数据库sql语句
            sql = "insert into 01_spider_jingdong(商品图片地址,商品价格,商品地址,商品配置,商品优惠,商品其他数据) values (%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, [item['商品图片地址'], item['商品价格'],item['商品地址'], item['商品配置'], item['商品优惠'],item['商品其他数据']])
            # 提交给数据库
            db.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('本次数据写入成功')

    """启动方法"""
    def run(self):
        res_data=self.html_data(url,headers)
        items=self.get_data(res_data)
        # self.create_table()
        self.write_data(items)

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    input_data=str(input('请输入搜索的商品名字：'))
    input_ye_data=int(input('请输入下载商品的页数：'))
    for i in range(1,input_ye_data+1):
        ye=2*i-1
        url='https://search.jd.com/Search?keyword={}BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={})&page={}&s=57&click=0'.format(input_data,input_data,ye)
        jingdong=Jingdong()
        jingdong.run()
    print('数据下载结束')






