import pymongo

###### 插入一条数据
# countent=pymongo.MongoClient('127.0.0.1',27017)
#
# # 数据库对象conuntent点上数据库名字school点上数据库表名classs
# student=countent.school.classs.insert_one({'name':'张三','age':33})

# 关闭数据库
# countent.close()

##### 插入多条数据
# countent=pymongo.MongoClient('127.0.0.1',27017)
#
# # 数据库对象conuntent点上数据库名字school点上数据库表名classs,注意：多条插入是在列表中的
# student=countent.school.classs.insert_many([{'name':'张三','age':33},{'name':'李四','age':44},{'name':'王五','age':55}])

# 关闭数据库
# countent.close()

##### 查询一条数据
# countent=pymongo.MongoClient('127.0.0.1',27017)
#
# # 数据库对象conuntent点上数据库名字school点上数据库表名classs
# student=countent.school.classs.find_one()
# print(student)

# 关闭数据库
# countent.close()

##### 条件查询一条数据
# countent=pymongo.MongoClient('127.0.0.1',27017)
#
# # 数据库对象conuntent点上数据库名字school点上数据库表名classs
# student=countent.school.classs.find_one({'age':33})
# print(student)

# 关闭数据库
# countent.close()

##### 如果直接使用find()获取所有数据就会出现一个惰性序列，获取惰性序列中数据的三种方法：for循环、list()、next()
countent=pymongo.MongoClient('127.0.0.1',27017)

# 数据库对象conuntent点上数据库名字school点上数据库表名classs
student=countent.school.classs
res=student.find()
# 获取惰性序列数据方法一：for循环
# for i in res:
#     print(i)
# 获取惰性序列数据方法二：list()
# print(list(res))
# 获取惰性序列数据方法三：next()
print(next(res))

# 关闭数据库
countent.close()