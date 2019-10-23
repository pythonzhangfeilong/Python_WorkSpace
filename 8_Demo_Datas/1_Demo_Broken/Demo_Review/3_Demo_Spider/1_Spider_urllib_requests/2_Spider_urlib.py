# 1、urllib中的urlopen()方法
# import urllib.request
# # 请求服务器
# response=urllib.request.urlopen('https://www.baidu.com')
# #调用read方法读取响应的数据
# print(response.read().decode())
# #获取响应状态吗
# print(response.status)
# #获取响应头部信息
# print(response.getheaders())
# #获取某个头部信息
# print(response.getheader('Server'))

# 带有参数的urllib请求
# import urllib.parse
# import urllib.request
# #利用parse方法解析数据，进行数据编码，并转换为字节的形式
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# #发送到固定的网址，进行请求
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# urllib中的是request方法
from urllib import request,parse
from fake_useragent import UserAgent
url = 'http://httpbin.org/post'
headers = {
    # 生成随机浏览器
    'User-Agent': UserAgent().random,
}
dict = {
    'name': 'for'
}
#把数据变成字节的形式
data = bytes(parse.urlencode(dict), encoding='utf8')
#进行网络请求
req = request.Request(url=url, data=data, headers=headers, method='POST')
# 请求响应
response = request.urlopen(req)
# 读取响应数据
print(response.read().decode('utf-8'))
















