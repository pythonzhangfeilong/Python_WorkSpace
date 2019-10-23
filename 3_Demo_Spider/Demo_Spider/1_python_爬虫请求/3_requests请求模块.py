# urllib这个模块在实现的功能的时候,构造代码比较复杂
#####requests是python实现的简单易用的HTTP库，使用起来比urllib简洁一些，死一次试用的时候需要pip install requests
#####requests的基本方法：
# import requests
# response=requests.get('https://www.baidu.com')
# # 打印状态码
# print('打印状态码:',response.status_code)
# # 打印请求url
# print('打印请求url:',response.url)
# # 打印请求头信息
# print('打印请求头信息:',response.headers)
# # 打印cookie信息
# print('打印cookie信息:',response.cookies)
# # 以文本形式打印页面源码
# print('以文本形式打印页面源码:',response.text)
# # 以字节流的形式打印
# print('以字节流的形式打印:',response.content)

#####requests的请求方式
    # import requests
    # requests.get('http://httpbin.org/get')
    # requests.post('http://httpbin.org/post')
    # requests.put('http://httpbin.org/put')
    # requests.delete('http://httpbin.org/delete')
    # requests.head('http://httpbin.org/get')
    # requests.options('http://httpbin.org/get')

#####带参数的get请求
# 第一种，直接将参数放在url中
# import requests
# response=requests.get('http://www.httpbin.org/get?name=gemey&age=22')
# # 以文本的形式打印页面的源码
# print(response.text)

# 第二种,经参数写在dict里，发送请求时params指定参数为dict
# import requests
# data={'name':'zhang','age':20}
# response=requests.get('http://www.httpbin.org/',params=data)
# # 以文本的像是打印页面的源码
# print(response.text)

# 解析json
# import requests
# response=requests.get('http://httpbin.org/get')
# # 以文本形式打印页面的源码
# print(response.text)
# # 解析json，response.json()方法同json.loads(response.text)
# print(response.json())
# print(type(response.json()))

# 保存一个二进制的文件，response.content二进制字节流
# import requests
# response=requests.get('http://gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/lvpics/w=1000/sign=9b38971c908fa0ec7fc7600d16a758ee/c8ea15ce36d3d5394fe85aec3b87e950342ab0cc.jpg')
# b=response.content
# with open('qiutian.jpg','wb') as f:
#     f.write(b)

# 为请求头添加信息
# from fake_useragent import UserAgent
# import requests
# # 随机产生一个浏览器
# headers={'User-Agent':UserAgent().random}
# # 给请求头添加信息
# response=requests.get('https://www.baidu.com',headers=headers)
# # 返回访问结果
# print(response.status_code)

# 使用代理
# 添加headers方法，代理参数也是一个dict
# import requests
# from fake_useragent import UserAgent
# # 设置代理地址，网上找的代理地址都是瞬间能用，建议使用稳定的地址
# proxies={'http':'182.34.33.215'}
# # 随机产生一个浏览器
# headers={'User-Agent':UserAgent().random}
# verify证书
# response=requests.get(url='http://www.baidu.com',headers=headers,proxies=proxies,verify=False)
# # 以文本的形式打印请求到的内容
# print(response.text)

# POST请求：
# import requests
# data={'name':'tom','age':22}
# 响应请求
# response=requests.post('http://httpbin.org/post', data=data)

# 获取cookie
# import requests
# response=requests.get('https://www.baidu.com')
# # 获取cookie
# print(response.cookies)
# # 查看cookie的类型
# print(type(response.cookies))
# for k,v in response.cookies.items():
#     print(k+':'+v)

# 会话维持
# import requests
# session=requests.Session()
# session.get('http://httpbin.org/cookies/set/number/12345')
# response=session.get('http://httpbin.org/cookies')
# print(response.text)

# 证书验证设置
import requests
import urllib3
urllib3.disable_warnings()  #从urllib3中消除警告
response = requests.get('https://www.12306.cn',verify=False)  #证书验证设为FALSE
print(response.status_code)



































