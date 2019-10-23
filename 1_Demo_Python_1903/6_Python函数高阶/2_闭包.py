#####闭包：
'''
闭包函数必须有内嵌函数
内嵌函数需要引用该嵌套函数的上一级namespace中的变量
闭包函数必须返回内嵌函数

Python装饰器使用的是闭包
'''

#####闭包的优点：
'''
使代码变的简洁
提高代码的拓展性
'''
# def outer():
#     def inner():
#         print('这个是闭包函数')
#     return inner
# outer()()

# 闭包的分析
# def outer(num):
#     def inner(num_inner):
#         print('inner函数传入的值是num_inner:%s'%num_inner)
#         return num + num_inner
#     return inner
# data=outer(5)
# print(data(20))

















