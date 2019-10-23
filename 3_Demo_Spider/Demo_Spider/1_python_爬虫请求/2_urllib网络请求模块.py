#####urllib.request模块
'''
    提供了最基本的构造HTTP请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理授权验证（authenticaton）、
    重定向（redirection)、浏览器Cookies以及其他内容。这个模块也可以做网络请求，主要目的是学习python中的requests。
'''

# 1、urlopen()方法：
'''
urllib.request.urlopen()函数用于实现对目标url的访问。
函数原型如下：urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)　
url:  需要打开的网址
data：Post提交的数据（bytes类型，则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式）
timeout：设置网站的访问超时时间
'''

# import urllib.request
# # 请求百度
# response=urllib.request.urlopen('https://www.baidu.com')
# # 调用read方法，读取响应的数据
# print(response.read().decode())
# # 获取响应状态码
# print('响应的状态码是：',response.status)
# # 获取响应的头部信息
# print('响应请求的头部信息是：',response.getheaders())
# # 获取某个头部信息
# print(response.getheaders('Server'))

# 发送带有date的请求
# import urllib.parse
# import urllib.request
# # 利用parse方法解析数据，进行数据编码，并转换为字节的形式，
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf8')
# # 发送到固定的网址进行请求
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 2、request方法
'''
    利用urlopen()方法可以实现最基本请求的发起，但这几个简单的参数并不足以构建一个完整的请求。如果请求中需要加入Headers
        等信息，就可以利用更强大的Request类来构建。
    class Request:
    def __init__(self, url, data=None, headers={},
                 origin_req_host=None, unverifiable=False,
                 method=None):
    第一个参数url用于请求URL，这是必传参数，其他都是可选参数。
    第二个参数data如果要传，必须传bytes（字节流）类型的。如果它是字典，可以先用urllib.parse模块里的urlencode()编码。
    第三个参数headers是一个字典，它就是请求头，在构造请求时通过headers参数直接构造，调用请求的add_header()方法添加。
'''
# from urllib import request,parse
# from fake_useragent import UserAgent
# url='http://httpbin.org/post'
# headers={'User-Agent':UserAgent().random}
# dict={'name':'zhang'}
# # 把数据变成字节的形式
# data=bytes(parse.urlencode(dict),encoding=('utf8'))
# # 进行网络请求
# req=request.Request(url=url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# # 输出读取到的响应的内容
# print(response.read().decode('utf8'))