import pymongo
# 连接MongoDB
mongo_connection=pymongo.MongoClient(host='127.0.0.1',port=27017)
# 连接数据库表
database=mongo_connection.mongoDB_one
# 给表插入数据，如果这个表存在就直接插入，不存在这个表时创建这个表插入
# 下面这个是表存在，直接插入
# database.MongoDB_One.insert({'id':1,'name':'张','age':21})

# 下面这个是表不存在，会创建这个表，在插入
database.MongoDB_Four.insert({'id':1,'name':'张','age':21})


