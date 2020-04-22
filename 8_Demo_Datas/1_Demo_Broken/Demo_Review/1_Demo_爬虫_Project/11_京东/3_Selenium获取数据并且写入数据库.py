from selenium import webdriver
# 键盘操作
from selenium.webdriver.common.keys import Keys
import pymysql
import time

class JingDong():
    """进行请求并且把页面滑动到底部"""
    def get_html(self,driver):
        url = 'https://www.jd.com/'
        # 进行请求
        driver.get(url=url)
        # 获取搜索框的id
        input_srpage = driver.find_element_by_id('key')
        inputs = str(input('请输入搜索商品的名字：'))
        # 在输入框输入
        input_srpage.send_keys(inputs)
        # 相当于点击了一下键盘的回车
        input_srpage.send_keys(Keys.ENTER)
        print('请等待页面数据加载完毕')

        # 通过JS控制滚轮滑动到页面底部
        for i in range(2):
            time.sleep(2)
            # 模拟滚动浏览器右侧的滚动条，滚动到底部，用来增加页数
            driver.execute_script('scrollTo(0,document.body.scrollHeight)')

        # 等待数据加载
        time.sleep(5)
        # 查找所有商品的div标签(注意是elements)
        shop_list = driver.find_elements_by_class_name('gl-item')
        print('共获取到{}件商品信息'.format(len(shop_list)))
        # 隐式等待10秒
        driver.implicitly_wait(10)
        return shop_list

    """逐一获取商品信息"""
    def get_shop_data(self,shop_list):
        items=[]
        for shop in shop_list:
            item={}
            shop_name = shop.find_element_by_css_selector('.p-name a').text.replace("\n", " ")
            shop_money = shop.find_element_by_css_selector('.p-price strong').text
            shop_url = shop.find_element_by_css_selector('.p-img a').get_attribute('href')
            shop_evaluate = shop.find_element_by_css_selector('.p-commit strong').text
            shop_shops_type = shop.find_element_by_css_selector('.p-shop a').text
            shop_other_data = shop.find_element_by_css_selector('.p-icons').text.replace("\n", " ")

            item['商品名字'] = shop_name
            item['商品价格'] = shop_money
            item['商品地址'] = shop_url
            item['商品评价数'] = shop_evaluate
            item['商品店铺类型'] = shop_shops_type
            item['商品其他数据'] = shop_other_data

            items.append(item)
        return items

    """创建数据库表"""
    def create_tables(self):
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db = pymysql.connect('127.0.0.1', 'root', '12345678', '01_spider_data', charset='utf8')
        # 使用cursor方法，创建一个游标对象，相当于操作者
        cursor = db.cursor()
        # 使用数据库游标对象，点上execute()直接写数据库sql语句
        cursor.execute("create table 03_spider_jingdong(id int primary key auto_increment,商品名字 varchar(1000) ,商品价格 varchar(1000),商品地址 varchar(2000),商品评价数 varchar (1000),商品店铺类型 varchar (1000),商品其他数据 varchar (1000))")
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
            sql = "insert into 03_spider_jingdong(商品名字,商品价格,商品地址,商品评价数,商品店铺类型,商品其他数据) values (%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql,[item['商品名字'], item['商品价格'], item['商品地址'], item['商品评价数'], item['商品店铺类型'], item['商品其他数据']])
            # 提交给数据库
            db.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('本次数据写入成功')

    """启动函数"""
    def run(self,driver):
        # 创建数据库表
        # self.create_tables()

        # 进行请求，获取商品列表
        shop_list=self.get_html(driver)
        # 逐一获取商品信息
        items=self.get_shop_data(shop_list)
        # 写入数据库
        self.write_data(items)

        # 等待3秒
        time.sleep(3)
        # 关闭浏览器
        driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    jingdong=JingDong()
    jingdong.run(driver)



























