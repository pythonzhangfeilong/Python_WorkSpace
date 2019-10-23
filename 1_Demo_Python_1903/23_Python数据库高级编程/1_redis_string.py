# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis对象，并且连接redis数据库
#         r=redis.Redis(host='127.0.0.1',port=6379)
#     except Exception as e:
#         print(e)

#####string增加，set方法
# 方法set，添加键值，如果添加成功返回True，如果添加失败返回False
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 使用set方法添加键值
#         result=r.set('name','zhang')
#         # 输出添加的结果
#         print(result)
#     except Exception as e:
#         print(e)

#####string获取，get方法
# 用键获取值，如果键不存在，返回None
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 使用get方法根据键查找值
#         result=r.get('name')
#         # 输出获取的结果
#         print(result)
#     except Exception as e:
#         print(e)

#####string修改，使用set方法修改
# 使用set方法也就是覆盖的一个操作
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 使用set方法修改
#         result=r.set('name','fei')
#         # 输出获取的结果
#         print(result)
#     except Exception as e:
#         print(e)

#####string修改，set方法修改，如果键已存在就进行修改，不存在创建键和值
# 其实也是一个覆盖修改的操作
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 使用set方法修改
#         result=r.set('zhang','fei')
#         # 输出获取的结果
#         print(result)
#     except Exception as e:
#         print(e)

#####string删除，使用delete删除,方法delete，删除键及对应的值，如果删除成功则返回受影响的键数，否则则返回0
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 使用delete方法指定键删除
#         result=r.delete('zhang')
#         # 输出删除的结果
#         print(result)
#     except Exception as e:
#         print(e)

#####string获取键，使用正则表达式获取键
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r=redis.Redis(host='127.0.0.1',port=6379)
#         # 获取所有的键
#         result=r.keys()
#         # 输出结果,所有的键构成一个列表，如果没有键返回一个空的列表
#         print(result)
#     except Exception as e:
#         print(e)



