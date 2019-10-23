import pymongo
# mongo数据库连接格式pymongo.MongoClient(mongodb://用户名：密码/@数据库地址：端口/数据库名字)
connect=pymongo.MongoClient('mongodb://user/@127.0.0.1:27017/admin')
print(connect)
