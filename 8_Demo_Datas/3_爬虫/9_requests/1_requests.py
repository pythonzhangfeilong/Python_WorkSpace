from fake_useragent import UserAgent
import requests
# 准备的url
url='http://www.baidu.com'
# 生成随机请求头
headers={'User-Agent':UserAgent().random}
# 获取请求响应
response=requests.get(url=url,headers=headers)
# 给响应内容设置编码格式
response.encoding='utf-8'
# 获取响应的源码
print(response.text)
# 获取响应的url
print(response.url)
# 获取响应的状态码
print(response.status_code)
# 获取响应的请求头
print(response.headers)
