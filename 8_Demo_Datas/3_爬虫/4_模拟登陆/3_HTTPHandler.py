from urllib import request
from fake_useragent import UserAgent

# 请求的url
url='http://www.baidu.com'

# 生成的随机请求头
headers={'User-Agent':UserAgent().random}

#定义一个HTTPHandler
http_handler=request.HTTPHandler()

# 创建openner，注册handler
openner=request.build_opener(http_handler)

# 构建请求
req=request.Request(url=url,headers=headers)

# 用自定义的handler请求服务器
response=openner.open(req)

print(response.read().decode('utf-8'))







