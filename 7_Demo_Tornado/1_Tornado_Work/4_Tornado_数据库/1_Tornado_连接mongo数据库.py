#####Tornado_数据库:
'''
Tornado自带处理MySQL请求的库。

使用MongoDB是因为它的简单性和便捷性：
    安装简单，并且能够和Python代码很好地融合。它结构自然，预定义数据结构不是必需的，很适合原型开发。
'''

#####使用PyMongo进行MongoDB基础操作
'''
PyMongo是一个简单的包装MongoDB客户端API的Python库。

pymongo是一个第三方模块，使用的时候需要进行pip install pymongo
'''

# 1、创建mongo数据库连接
import pymongo
# mongo数据库连接格式pymongo.MongoClient(mongodb://用户名：密码/@数据库地址：端口/数据库名字)
connect=pymongo.MongoClient('mongodb://user/@127.0.0.1:27017/first_database')
print(connect)

# 2、mongo数据库常见的操作
'''
1、	新增：db  点上  数据表的名字  点上  insert  （{“id”：1，“key”：“value”}）
db.MongoDB_One.insert({'id':1,'name':'huhehaote','age':'27'});

删除：db  点上  数据表的名字  点上  remove  ({条件})
2、	
db.MongoDB_One.remove({'name':'张'});

3、修改：db  点上  数据表的名字  点上  update  {‘把这个里面的内容’}，{$set:{修改成这里的内容}}
db.MongoDB_One.update({'id':5,'name':'呼和浩特','age':'26'},{$set:{'id':6,'name':'内蒙古','age':'26'}});


4、查表中的全部数据：db  点上  数据表的名字  find()
db.MongoDB_One.find()

5、根据条件查询：db  点上  数据库的名字  find  ({条件})
db.MongoDB_One.find({'name':'张'});

6、创建一张表：db 点上createCollection（‘表的名字’）；
db.createCollection("MongoDB_Three");		

'''





























