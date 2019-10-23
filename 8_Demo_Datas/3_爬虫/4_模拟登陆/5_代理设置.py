from urllib import request
from fake_useragent import UserAgent
url='http://www.baidu.com/s?wd=ip'

# 生成随机请求头
headers={'User-Agent':UserAgent().random}

# 代理ip由字典组成（注意：如果使用的ip是有账号和密码的，格式：http://账号:密码@ip:端口）
prox={
    'http':'http://47.94.90.249:4111'
}

# 定义handler,参数是代理ip
handler=request.ProxyHandler(proxies=prox)

# 创建opnner。注册handler
openner=request.build_opener(handler)

req=request.Request(url=url,headers=headers)

response=openner.open(req)

res=response.read().decode('utf-8')

print(res)










