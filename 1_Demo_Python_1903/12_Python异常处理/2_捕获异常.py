# print('--test01--')
# try:
#     # 没有变量，会提示变量没有被定义
#     print(name)
# except:
#     print('名字没有被定义，运行个毛')
# print('--test02--')

#####捕获多个异常
# 下面这种捕获异常的方式是只捕获发生的死一个异常，不管其他异常
# try:
#     print(name)
#     f=open('123.txt','r')
# except :
#     print('只捕获了name没有被定义')

# 用异常的父类Exeception来捕获多个异常
# try:
#     print(name)
#     f=open('123.txt','r')
# except Exception:
#     print(1)

# 用元组来指定多个异常进行捕获
# try:
#     print(name)
#     f=open('123.txt','r')
# except (NameError,FileNotFoundError):
#     print('第一个异常是%s'%NameError)
#     print('第二个异常是%s'%FileNotFoundError)

# 在except后面不加任何异常，捕获所有的异常
# try:
#     print(name)
#     f=open('123.txt','r')
# except:
#     print('有异常，就不打印')







