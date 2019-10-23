# Python连接redis
# import redis
# r_connect=redis.Redis(host='127.0.0.1',port=6379)
# print(r_connect)

# set()方法添加键值，如果添加成功返回True，如果添加失败返回False
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r_connect = redis.Redis(host='127.0.0.1', port=6379)
#         # 连接对象点上set方法添加键为name，值为zhang
#         result=r_connect.set('name','zhang')
#         # 删除添加的结果
#         print(result)
#     except Exception as e:
#         print(e)

# get()方法获取键值，如果获取到就返回值，如果没有获取到就返回None
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r_connect = redis.Redis(host='127.0.0.1', port=6379)
#         # 连接对象点上set方法添加键为name，值为zhang
#         result=r_connect.get('name')
#         # 删除添加的结果
#         print(result)
#     except Exception as e:
#         print(e)

# set()方法添加键值，如果键重复，那么就会覆盖以前的值，也就是修改
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r_connect = redis.Redis(host='127.0.0.1', port=6379)
#         # 连接对象点上set方法添加键为name，值为zhang
#         result=r_connect.set('age','18')
#         # 删除添加的结果
#         print(result)
#     except Exception as e:
#         print(e)

# delete()删除对应的键值，删除成功返回受影响的值和受影响的行数，删除失败返回0
# import redis
# if __name__ == '__main__':
#     try:
#         # 创建redis链接对象
#         r_connect = redis.Redis(host='127.0.0.1', port=6379)
#         # 连接对象点上set方法添加键为name，值为zhang
#         result=r_connect.delete('name')
#         # 删除添加的结果
#         print(result)
#     except Exception as e:
#         print(e)

# keys()获取所有的键
import redis
if __name__ == '__main__':
    try:
        # 创建redis链接对象
        r_connect = redis.Redis(host='127.0.0.1', port=6379)
        # 连接对象点上kyes()获取所有的键
        result=r_connect.keys()
        # 删除添加的结果
        print(result)
    except Exception as e:
        print(e)




















