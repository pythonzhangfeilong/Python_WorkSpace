from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql

class SuNing():
    """请求页面并且获取页面商品列表"""
    def get_html(self,driver):
        url = 'https://www.suning.com/'
        driver.get(url=url)
        # 获取搜索框的id
        get_html_ssid=driver.find_element_by_id('searchKeywords')
        get_html_ssid.send_keys('手机')
        get_html_ssid.send_keys(Keys.ENTER)
        # 通过JS控制滚轮滑动到页面底部
        for i in range(5):
            time.sleep(2)
            # 模拟滚动浏览器右侧的滚动条，滚动到底部，用来增加页数
            driver.execute_script('scrollTo(0,document.body.scrollHeight)')

        # 获取包含商品信息的列表
        shop_list=driver.find_elements_by_class_name('item-wrap')
        print('共获取到{}件商品信息'.format(len(shop_list)))
        return shop_list


    """获取想要的数据"""
    def get_data(self,shop_list):
        items = []
        for shop in shop_list:
            item = {}
            shop_url = shop.find_element_by_css_selector('.title-selling-point a').get_attribute('href')
            shop_money = shop.find_element_by_css_selector('.price-box span').text
            shop_name = shop.find_element_by_css_selector('.title-selling-point a').text
            shop_configure = shop.find_element_by_css_selector('.info-config em').text

            # 评价
            # shop_evaluate=shop.find_element_by_css_selector('.ad-label').text
            # 店铺类型
            # shop_shops_type=shop.find_element_by_css_selector('.store-stock a').text
            # 商品其他数据
            # shop_other_data=shop.find_element_by_css_selector('.sales-label span').text

            item['商品名字'] = shop_name
            item['商品价格'] = shop_money
            item['商品配置'] = shop_configure
            item['商品地址'] = shop_url

            items.append(item)
        return items

    """创建数据库表"""
    def create_table(self):
        db=pymysql.connect('127.0.0.1','root','12345678','01_spider_data',charset='utf8')
        cursor=db.cursor()
        cursor.execute("create table 04_spider_suning(id int primary key auto_increment,商品名字 varchar(1000),商品价格 varchar(1000),商品配置 varchar (1000),商品地址 varchar(1000))")
        cursor.close()
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
            sql = "insert into 04_spider_suning(商品名字,商品价格,商品配置,商品地址) values (%s,%s,%s,%s);"
            cursor.execute(sql,[item['商品名字'], item['商品价格'], item['商品配置'], item['商品地址']])
            # 提交给数据库
            db.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()
        print('本次数据写入成功')

    """启动函数"""
    def run(self,driver):
        shop_list=self.get_html(driver)
        items=self.get_data(shop_list)
        # self.create_table()
        self.write_data(items)

        time.sleep(3)
        driver.quit()

if __name__ == '__main__':
    driver=webdriver.Chrome()
    suning=SuNing()
    suning.run(driver)























