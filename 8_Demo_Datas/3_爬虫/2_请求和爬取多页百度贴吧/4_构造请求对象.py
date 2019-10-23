from urllib import request
from urllib import parse
from fake_useragent import UserAgent

url='http://www.baidu.com'

# 产生随机请求头
headers={
    'User-Agent':UserAgent().random
}

# 构造请求对象
response=request.Request(url=url,headers=headers)

# 发起请求
response_s=request.urlopen(response)

# 获取请求的状态码
print(response_s.getcode())
