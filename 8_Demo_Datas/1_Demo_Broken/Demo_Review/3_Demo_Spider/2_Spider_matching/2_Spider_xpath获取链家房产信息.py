import requests
from lxml import etree
from fake_useragent import UserAgent
import pymysql,warnings

#创建数据库，生成表结构
db = pymysql.connect("localhost","root","",charset="utf8")
cursor = db.cursor()
create_db = "create database if not exists Lianjiadb character set utf8"
use_db = "use Lianjiadb"
create_tab = "create table if not exists housePrice(id int primary key auto_increment,housename varchar(50),totalprice varchar(50))charset=utf8"
warnings.filterwarnings("ignore")#由于已经有数据库了所以会有警告信息在这里让程序性忽略
cursor.execute(create_db)
cursor.execute(use_db)
cursor.execute(create_tab)

headers  = {
    'User-Agent':UserAgent().random
}

base_url = 'https://bj.lianjia.com/ershoufang/pg{}/'
#响应HTML交给parse_page解析
def load_page(url):
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            print('页面请求完毕')
            return res.text
    except:
        print('网络访问错误')
#解析HTML拿到想要的数据
def parse_page(html):
    xpath_content = etree.HTML(html)
    xpath_datas = xpath_content.xpath("//*[@class='info clear']")
    for data in xpath_datas:
        title = data.xpath('./div[1]/a/text()')
        price = data.xpath('./div[4]//div[@class="totalPrice"]/span/text()')
        # print(place)
        new_data = zip(title,price)
        for tup_data in new_data:
            insert_mysql(tup_data)
    print('数据写入完毕')
#插入到指定的数据库中
def insert_mysql(data):
    insert_data = "insert into housePrice(housename,totalprice) values(%s,%s)"
    if data:
        cursor.execute(insert_data,list(data))
        db.commit()
def main():
    for i in range(1,10):
        url = base_url.format(str(i))
        html = load_page(url)
        parse_page(html)
if __name__ == '__main__':
    main()
