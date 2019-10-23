#####装饰器:在不修改原有代码的基础上添加新的功能
# def outer(func):
#     def inner():
#         func()
#         print('from china')
#     return inner
# @outer
# def func1():
#     print('My name is zhangsan')
# @outer
# def func2():
#     print('My name is lisi')
#
# def main():
#     func1()
#     func2()
# main()

#####装饰器传递参数
# def outer(func):
#     def inner(name):
#         func(name)
#         print('name的值是%s'%name)
#     return inner
# @outer
# def func1(name):
#     print('%s今年23岁'%name)
# func1('张飞龙')

#####更加通用的装饰器
def outer(func):
    def inner(*args,**kwargs):
        function_func=func(*args,**kwargs)
        print(function_func)
    return inner
@outer
def func1(a,b=1):
    return a+b
func1(5,6)












