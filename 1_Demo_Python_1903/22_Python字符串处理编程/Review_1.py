#####json.dumps()和json.loads()适用于处理json字符串

#####json.dump()和json.load()适用于处理json文本

# 下面是字符串操作
#####json.dumps()把python对象转换为json字符串
# import json
# data={'name':'zhang','age':23,'address':'huhehaote'}
# # 使用json.dumps()将python对象转换为json字符串
# json_data=json.dumps(data)
# print(json_data)

# 下面是文本操作
#####json.dump()把python对象转换为json文本
# 写入数据
# import json
# data={'name':'zhang','age':23,'address':'huhehaote'}
# # 打开Review_data_json.json文件写入数据
# with open('Review_data_json.json','w',encoding='utf-8') as write_data:
#     json.dump(data,write_data)

# 读取数据
# import json
# # 打开Review_data_json.json文件读取数据
# with open('Review_data_json.json','r',encoding='utf-8') as read_data:
#     # 打印读取到的数据
#     print(json.load(read_data))

#####json最新的模块是demjson,demjson.encode()是将python对象转换为json字符串,demjson.decode()是将json字符串转换为python对象
# import demjson
# data={'name':'zhang','age':23,'address':'huhehaote'}
# # 使用demjson模块将python对象转换为json字符串
# data_json=demjson.encode(data)
# # 输出
# print(data_json)

#####使用demjson.decode()将特殊的json字符串转换为python对象
# import demjson
# data = '{a:"000001_Unit_1. Hi,Birdie.mp3",b:"000005_Unit_2. Good morning,Miss Wang..mp3",c:"000008_Unit_3. What\'s your name_.mp3"}'
# data_json=demjson.decode(data)
# print(data_json)

#####如何把嵌套的字典对象封装到json中
# import json
# data_a={'data':{'name':'zhang','age':18}}
# data_b=json.dumps(data_a)
# print(data_b)

#####hashlib提供了常见的MD5和SHA1算法
# 将字符串编码为MD5
# import hashlib
# md5=hashlib.md5()
# md5.update('my name is zhangfeilong'.encode())
# print(md5.hexdigest())

# 将字符串编码为SHA1，与MD5的操作一致
# import hashlib
# sha1=hashlib.sha1()
# sha1.update('my name is zhangfeilong'.encode())
# print(sha1.hexdigest())

#####使用MD5加密登陆
# import hashlib
# # 创建一个空的字典，用户名就是键，密码就是值
# dict_kong={}
# # 使用while循环输入3组用户名和密码
# n=0
# while n<3:
#     # 将手动输入的密码储进行MD5加密存起来
#     name=input('请输入用户名：')
#     pwd=input('请输入密码：')
#     # 把密码使用hashlib加密为MD5
#     md5=hashlib.md5()
#     # 将内容编码为MD5
#     md5.update(pwd.encode('utf-8'))
#     # 返回MD5加密摘要，也就是加密好的内容
#     md5_pwd=md5.hexdigest()
#     # 把用户名和加密后的密码放入字典中
#     for i in range(3):
#         dict_kong[name]=md5_pwd
#     n=n+1
# else:
#     print(dict_kong)


dict_user_passworld={'zhang': '202cb962ac59075b964b07152d234b70', 'fei': '250cf8b51c773f3f8dc8b4be867a9a02', 'long': '68053af2923e00204c3ca7c6a3150cf7'}

# 创建一个登陆类
import hashlib
class Login():
    # 默认属性方法
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd
    def login_jy(self):

        if self.user==dict_user_passworld['zhang'] and self.pwd==dict_user_passworld['202cb962ac59075b964b07152d234b70']:

            print('登陆成功')
        else:
            print('用户名或密码错误，登陆失败')

if __name__ == '__main__':
    user=input('请输入用户名：')
    passworld=input('请输入密码：')
    # 将输入的密码进行MD5加密
    md5 = hashlib.md5()
    md5.update(passworld.encode())
    md5_passworld = md5.hexdigest()
    # 将类实例为对象，并传值
    user_login=Login(user,md5_passworld)
    # 类对象调用方法
    user_login.login_jy()




# # 定义一个空字典，把参数变成字典，再与账户和密码存的字典比较
#         dict_kong={}
#         # 把登陆输入的用户名和密码放入字典中
#         dict_kong[self.user]=self.pwd




