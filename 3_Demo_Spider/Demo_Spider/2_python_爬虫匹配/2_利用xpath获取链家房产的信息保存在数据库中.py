from lxml import etree
import requests
import pymysql
import warnings
from fake_useragent import UserAgent
# 创建数据库，生成数据库表
db=pymysql.connect('127.0.0.1','root','',charset='utf8')
# 创建游标对象
cursor=db.cursor()
# 如果不存在if not exists创建表
create_db = "create database if not exists Lianjiadb character set utf8"
use_db = "use Lianjiadb"
create_tab = "create table if not exists housePrice(id int primary key auto_increment,housename varchar(50),totalprice varchar(50))charset=utf8"
warnings.filterwarnings("ignore")#由于已经有数据库了所以会有警告信息在这里让程序性忽略
cursor.execute(create_db)
cursor.execute(use_db)
cursor.execute(create_tab)

# 准备链接地址
base_url='https://bj.lianjia.com/ershoufang/pg{}/'
# 随机生成浏览器
headers={'User-Agent':UserAgent().random}
# 获取响应
def func_request(url):
    try:
        # 获取请求响应的结果
        response=requests.get(url,headers)
        # 如果请求的响应结果是200
        if response.status_code==200:
            print('请求完毕')
            # 以文本的形式返回请求的信息
            return response.text
    except:
        print('网络错误')

# 解析html，过去自己想要的数据
def func_xpath_hq(html):
    # 构建解析对象
    xpath_content=etree.HTML(html)
    # 匹配获取当前界面的所有元素
    xpath_datas=xpath_content.xpath('//*[@class="info clear"]')
    # for循环逐一获取信息
    for data in xpath_datas:
        # 获取头部信息,因为上面已经匹配到位了，所以直接.当前路径下往下写
        title=data.xpath('./div[1]/a/text()')
        # 获取标签中的房价信息
        price=data.xpath('./div[4]//div[@class="totalPrice"]/span/text()')
        # 利用zip放下将俩个数据拼接形成新的数据格式
        new_data=zip(title,price)
        # 使用for循环把数据写入数据库中
        for tup_data in new_data:
            insert_mysql(tup_data)
    print('数据写入完毕')
# 写入数据库
def insert_mysql(data):
    insert_data='insert into housePrice(housename,totalprice)values (%s,%s)'
    if data:
        cursor.execute(insert_data,list(data))
        # 提交给数据库
        db.commit()

def func_main():
    for i in range(1,10):
        # 拼接url
        url=base_url.format(str(i))
        html=func_request(url)
        func_xpath_hq(html)
if __name__ == '__main__':
    func_main()









