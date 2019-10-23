import pymongo
# 连接数据库
conn=pymongo.MongoClient('127.0.0.1',27017)

# 连接到集合
tables=conn.student.student

# 查询一条数据
# res=tables.find_one()
# print(res)

# 使用find()查询数据时，会出现一个惰性序列<pymongo.cursor.Cursor object at 0x00000142C0968518>
# res=tables.find()
# print(res)

# 获取惰性序列里面的值可以使用：循环、列表、next
# 循环
# for var in res:
#     print(var)
# 列表
# print(list(res))
# next
# print(next(res))

# count()获取集合中有多少数据
# print(tables.find().count())

# 条件查询
print(tables.find_one({'age':30}))
# 关闭数据库
conn.close()








