#####在pycharm的Terminal中 pip install pymysql

#####轮子安装网站https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

#####wheel是轮子安装的必要模块，所以需要 pip install wheel

#####轮子安装语法pip install 轮子文件名

#####换源安装，会解决网速慢的问题，语法： pip insatll -i 国内源
'''
国内源：
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
'''

#####数据库操作关键字
'''
创建连接     connect
实例化游标   cursor
执行sql语句 execute
提交修改     commit
事务回滚     rollback
关闭游标和链接 close
'''

#####脚本连接数据库,且创建表
# import pymysql
# # 连接数据库，参数分别为本地地址、用户名、密码、数据库、字符集(数据库中的字符集认的是utf8，不是utf-8)
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 使用cursor方法，创建一个游标对象，相当于操作者
# cursor=mysql_db.cursor()
# # 使用数据库游标对象，点上execute()直接写数据库sql语句
# cursor.execute("create table table_one(id int primary key auto_increment,name varchar(30) ,age int )")
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####commit主要是为了配合修改、增加、删除来使用的

#####添加数据
# import pymysql
# # 连接数据库,参数分别为数据库链接、用户名、密码、数据库、字符集
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 使用cursor创建数据库游标
# cursor=mysql_db.cursor()
# # 使用游标对象点上execute编写执行sql语句
# cursor.execute("insert into table_one(name,age)value ('张飞龙',23)")
# # 插入数据是需要向数据库提交的
# mysql_db.commit()
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####删除(drop是强制删除，delete删除后需要提交)
# import pymysql
# # 连接数据库
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 使用cursor创建数据库游标
# cursor=mysql_db.cursor()
# # 使用游标对象点上execute编写执行sql
# cursor.execute("delete from table_one where id = 3")
# # 提交给数据库
# mysql_db.commit()
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####手动输入插入数据库的数据
# import pymysql
# # 连接数据库
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 创建游标对象
# cursor=mysql_db.cursor()
# # 编写sql
# sql="insert into table_one(name,age)value (%s,%s)"
# # 自定义输入内容
# while True:
#     name=input('请输入name:')
#     age=input('请输入age:')
#     # 使用游标对象点上execute()编写执行sql
#     cursor.execute(sql,[name,age])
#     # 提交给数据库
#     mysql_db.commit()
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####修改
# import pymysql
# # 连接数据库
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 创建游标
# cursor=mysql_db.cursor()
# # 使用游标对象点上execute()编写执行数据库语句
# cursor.execute("update table_one set name='李四' where id = '6'")
# # 提交给数据库
# mysql_db.commit()
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####数据库查询
'''
fetchone(): 	该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 	接收全部的返回结果行.
'''
# import pymysql
# # 连接数据库
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# # 创建游标
# cursor=mysql_db.cursor()
# # 使用用游标对象点上execute编写执行sql
# cursor.execute("select * from table_one where id = '4'")
# # 获取一条数据
# # data=cursor.fetchone()
# # 获取全部数据(查的是表)
# # data=cursor.fetchall()
# # 输出
# print(data)
# # 关闭游标
# cursor.close()
# # 关闭数据库
# mysql_db.close()

#####事物回滚rollback()
'''
事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。 
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
'''
# import pymysql
# mysql_db=pymysql.connect('127.0.0.1','root','','database_one',charset='utf8')
# cursor=mysql_db.cursor()
# sql ="delete from test_sql where age ='%d'%(20)"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
# # 向数据库提交
#     mysql_db.commit()
# except:
#     # 发生错误时回滚
#     mysql_db.rollback()

#####数据库搜索引擎
'''
在这里咱们主要了解一下，MySQL有两大搜索引擎，一个是InnoDB 、MyISAM他们的具体区别是：MyISAM类型不支持事务处理等高级处理，
 而InnoDB类型支持。MyISAM类型的表强调的是性能，其执行速度比InnoDB类型更快，但是不提供事务支持，
 而InnoDB提供事务支持以及外部键等高级数据库功能。             
mysql>show engines； 查看数据库引擎
'''












