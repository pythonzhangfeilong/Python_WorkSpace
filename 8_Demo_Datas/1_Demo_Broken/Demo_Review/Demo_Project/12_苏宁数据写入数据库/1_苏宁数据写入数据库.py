from bs4 import BeautifulSoup
import requests
import pymysql
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

class Suning():
    """网页请求"""
    def get_html(self,url,headers):
        response=requests.get(url=url,headers=headers)
        response.encoding=response.apparent_encoding
        if response.status_code==200:
            res=response.text
            return res

    """获取需要的数据"""
    def get_data(self,res_data):
        soup=BeautifulSoup(res_data,'lxml')
        shop_data_list=soup.select('.product-box ')
        items=[]

        for shop_data in shop_data_list:
            shop_img='http:'+shop_data.select('.img-block img')[0].get('src')
            shop_url='http:'+shop_data.select('.img-block a')[0].get('href')
            shop_jianjie=shop_data.select('.title-selling-point a')[0].get_text()
            shop_peizhi=shop_data.select('.info-config')[0].get_text()
            shop_shops_name=shop_data.select('.store-stock')[0].get_text()

            item={}
            item['shop_img'] = shop_img
            item['shop_url'] = shop_url
            item['shop_jianjie'] = shop_jianjie
            item['shop_peizhi'] = shop_peizhi
            item['shop_shops_name'] = shop_shops_name

            items.append(item)
        return items

    """创建数据库表"""
    def create_table(self):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db = pymysql.connect('127.0.0.1', 'root', '12345678', '01_spider_data', charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor = db.cursor()
        # 使用数据库游标对象，点上execute()直接写数据库sql语句
        cursor.execute("create table 02_spider_suning(id int primary key auto_increment,商品图片地址 varchar(100) ,商品详情地址 varchar(100),商品简介 varchar(200),商品配置 varchar (100),商品店铺名字 varchar (100))")
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('数据库表创建成功')

    """把数据写入数据库"""
    def write_data(self,items):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db = pymysql.connect('127.0.0.1', 'root', '12345678', '01_spider_data', charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor = db.cursor()
        for item in items:
            # 使用数据库游标对象，点上execute()直接写数据库sql语句
            sql="insert into 02_spider_suning(商品图片地址,商品详情地址,商品简介,商品配置,商品店铺名字) values (%s,%s,%s,%s,%s);"
            cursor.execute(sql,[item['shop_img'], item['shop_url'], item['shop_jianjie'], item['shop_peizhi'], item['shop_shops_name']])
            # 提交给数据库
            db.commit()
            # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('本次数据写入成功')

    """启动函数"""
    def run(self):
        res_data=self.get_html(url=url,headers=headers)
        items=self.get_data(res_data)
        # self.create_table()
        self.write_data(items)

if __name__ == '__main__':
    url='http://list.suning.com/0-20006-0.html?safp=d488778a.phone2018.103327226421.1&safc=cate.0.0'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    suning=Suning()
    suning.run()
































