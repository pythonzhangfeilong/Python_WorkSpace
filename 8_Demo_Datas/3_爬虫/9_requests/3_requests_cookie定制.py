import requests
from fake_useragent import UserAgent

# 保存登录的cookie
session=requests.Session()

url='https://www.kuaidaili.com/login/'

headers={'User-Agent':UserAgent().random}

data={
    'next': '',
    'kf5_return_to':'' ,
    'username': '1634025627@qq.com',
    'passwd': 'ZFL152308',
}
# 向登陆地址发起请求，目的是先拿到登陆时的cookie，然后把cookie保存在session变量里（注意：携带的参数的请求是post）
response=session.post(url=url,headers=headers,data=data)

new_url='https://www.kuaidaili.com/usercenter/'

# 使用带有cookie值得session变量向个人主页发起请求
new_response=session.get(url=new_url,headers=headers)

res=new_response.text

with open('kuaidaili.html','w',encoding='utf-8') as f:
    f.write(res)

##### session和cookie登录时的原理都是先把登陆时的cookie保存下来，然后用带有cookie的变量请求登陆













