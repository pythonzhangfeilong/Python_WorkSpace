# json.dumps()编码为json字符串
# import json
# data={
#     'name':'zhang',
#     'age': 18,
#     'list':[1,2,3,4,5]
# }
# # 利用json的dumps方法把数据转换为json字符串
# json_data=json.dumps(data)
# print(type(json_data))
# print(json_data)

# json.load()解码json数据
# 写入json数据
# import json
# json_data={"name": "zhang", "age": 18, "list": [1, 2, 3, 4, 5]}
# with open('data.json','w',encoding='utf-8')as f:
#     # 写入编码为json的数据
#     f.write(str(json.dumps(json_data)))

# 读取json数据
# import json
# with open('data.json','r',encoding='utf-8') as f:
#     json_data=json.load(f)
#     print(json_data)

# demjson
# import demjson
# data = '{a:"000001_Unit_1. Hi,Birdie.mp3",b:"000005_Unit_2. Good morning,Miss Wang..mp3",c:"000008_Unit_3. What\'s your name_.mp3"}'
# # demjson.decode()解码json数据为Python对象
# data_json=demjson.decode(data)
# print(type(data_json))
# print(data_json)
# # demjson.encode()将Python对象编码为json数据
# data_json=demjson.encode(data)
# print(type(data_json))
# print(data_json)

# 嵌套字典封装为json数据
# import json
# data={'datas':{'name':'zhang','age':18}}
# data_json=json.dumps(data)
# print(data_json)
#
# import demjson
# data={'datas':{'name':'zhang','age':18}}
# data_json=demjson.encode(data)
# print(data_json)

# 常见的MD5算法，计算一个md5的值
# import hashlib
# # 创建一个md5算法对象
# md5_object=hashlib.md5()
# # 利用update方法将字符串编码
# md5_object.update('0471'.encode())
# # 输出
# print(md5_object.hexdigest())

# 常见的SHA1算法，计算一个SHA1的值
# import hashlib
# # 创建一个SHA1算法对象
# sha1_object=hashlib.sha1()
# # 利用update方法将字符串编码
# sha1_object.update('0471'.encode())
# # 输出
# print(sha1_object.hexdigest())

# base64
# 利用b64decode()方法将字符串解码为base64格式
import base64
data=base64.b64decode('YmluYXJ5AHN0cmluZw==')
print(data.decode())


















