# 1、requests中常用的方法
# import requests
# # 请求响应
# response=requests.get('https://www.baidu.com')      # get()请求指定的url
# print('请求状态码:',response.status_code)             # status_code请求状态码
# print('请求的url:',response.url)                      # url请求的url
# print('请求头信息:',response.headers)                 # headers打印请求头信息
# print('请求的cookies:',response.cookies)              # cookies打印请求的cookies
# print('文本的形式打印网页的源码:',response.text)       # text以文本的形式打印网页的源码
# print('以字节流的形似打印网页源码:',response.content)  # content以字节流的形似打印网页源码

# 2、直接将参数放在url内
# import requests
# response = requests.get('http://httpbin.org/get?name=gemey&age=22')
# # 以文本的形式打印网页的源码
# print(response.text)

# 3、先将参数填写在dict中，发起请求时params参数指定为dict
# import requests
# data = {
#     'name': 'for',
#     'age': 20
# }
# # 使用get方法请求指定的地址，并且params参数指定为dict
# response = requests.get('http://httpbin.org/get', params=data)
# # 以文本的形似打印网页的源码
# print(response.text)

# 4、解析json
# import requests
# response = requests.get('http://httpbin.org/get')
# # 以文本的形式打印网页的源码
# print(response.text)
# #response.json()方法同json.loads(response.text)
# print(response.json())
# # 查看类型
# print(type(response.json()))

# 简单的保存一个二进制文件，二进制内容为response.content（字节的形式）
# import requests
# # 请求响应，get访问指定url
# response=requests.get('http://p0.so.qhmsg.com/sdr/400__/t0179d7e549f15e2e75.jpg')
# # 创建一个字二进制内容为response.content（字节的形式）对象
# b_dir=response.content
# # 打开一个文件
# with open('网图.jpg','wb')as f:
#     # 将以字节形式打开的文件写入f中
#     f.write(b_dir)

# 固定添加请求头信息headers
# import requests
# # 设置指定的headers
# headers={
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36'
# }
# # 请求响应
# response=requests.get('https://www.baidu.com/',headers=headers)
# # 输出页面的请求头信息
# print(response.headers)

# 设置代理
# import requests
# # 导入UserAgent为了生成随机的请求头信息也就是随机的浏览器
# from fake_useragent import UserAgent
# # 设置代理
# proxies = {
#     'http':'119.57.105.25:53281',
# }
# # 随机生成浏览器
# headers  ={
#     'user_agent':UserAgent().random
# }
# # 请求响应，proxies=proxies设置代理,关闭验证verify=False
# response = requests.get(url='http://www.baidu.com',headers=headers,proxies=proxies,verify=False)
# # 以文本的形式打印源码
# print(response.text)

# 基本post请求
# import requests
# # 设置参数
# data = {'name':'tom','age':'22'}
# # 使用post方法请求指定url，data传递数据
# response = requests.post('http://httpbin.org/post', data=data)
# # 查看网页的请求响应码
# print(response.status_code)

#获取cookie
# import requests
# # 请求响应
# response=requests.get('https://www.baidu.com/')
# # 获取请求的cookies
# print('请求cookies：',response.cookies)
# # 查看请求cookies的类型
# print('请求cookies类型：',type(response.cookies))
# # 以字典的形式显示cookies
# for k,v in response.cookies.items():
#     print('请求cookies：',k+':'+v)

# 会话维持
# import requests
# # 创建请求session对象
# session = requests.Session()
# # 给session对象使用set添加number/12345
# session.get('http://httpbin.org/cookies/set/number/12345')
# # 请求响应
# response = session.get('http://httpbin.org/cookies')
# # 以文本形式输出页面内容
# print(response.text)

# 证书验证
import requests
from requests import urllib3
#从urllib3中消除警告
urllib3.disable_warnings()
# 证书验证设为FALSE
response = requests.get('https://www.12306.cn',verify=False)
# 获取响应的状态码
print(response.status_code)






