import pymysql
class Pymysql():
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
        # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
        db=pymysql.connect('127.0.0.1','root','12345678','fang_data',charset='utf8')
        # 使用cursor创建数据库游标
        cursor=db.cursor()
        # 使用游标对象点上execute编写执行sql
        cursor.execute("insert into spider_fang(name,addr,money,phone) values ({},{},{},{});".format())
        # 提交给数据库
        db.commit()
        # 关闭游标
        cursor.close()
        # 关闭数据库
        db.close()