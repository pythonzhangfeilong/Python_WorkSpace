#1、resquest中的常用方法
'''
    request.urlopen()                   请求指定的url
    type(response)                      查看响应的类型
    response.read()                     读取全部的响应内容
    response.readline()                 读取一行响应内容
    response.readlines()                读取全部响应内容
    response.read().decode('UTF-8')     响应解码
    response.getcode()                  查看响应的状态
    response.geturl()                   查看响应的url
    response.getheaders()               查看响应的请求头
'''
from urllib import request
# 请求模块点上打开地址的方法就是响应
response=request.urlopen('http://www.baidu.com')

# 查看响应的类型
# print('页面的相应类型是：',type(response))

# 响应response的read()方法,返回的是二进制的数据
# print('页面二进制响应',response.read())

# 响应response的read()方法,查看返回的内容（encode是编码，decode是解码）
res=response.read().decode('UTF-8')
print(res)
with open('baidu.html','w',encoding='UTF-8') as baidu:
    baidu.write(res)
# getcode()查看页面响应状态
print('页面响应状态：',response.getcode())
# geturl()查看请求的url
print('请求的页面：',response.geturl())
# getheaders(),查看请求头信息
print('页面请求头信息：',response.getheaders())
# 查看模块中的方法
print(dir(response))































