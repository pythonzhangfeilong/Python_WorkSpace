import pymongo

# 连接MongoDB数据库,参数：地址，端口
conn=pymongo.MongoClient('127.0.0.1',27017)

# 创建数据库名称,conn.数据库名称
dbs=conn.student

# 创建集合(也就是创建表)，连续的创建表和集合并且添加数据就使用后面的方法tables=conn.student.student.insert_many()
tables=dbs.student

data1={
    'name':'张三',
    'age':20,
    'gender':'男'
}

data2={
    'name':'张三',
    'age':20,
    'gender':'男'
}

data3={
    'name':'张三',
    'age':20,
    'gender':'男'
}

data4={
    'name':'张三',
    'age':20,
    'gender':'男'
}

data5={
    'name':'张三',
    'age':30,
    'gender':'男'
}

# 添加数据
tables.insert_one(data5)      # 插入一条
# tables.insert_many([data1,data2,data3,data4,data5])     # 插入多条

# 关闭连接
conn.close()