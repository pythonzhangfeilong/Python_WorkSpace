#####raise触发一个异常
# 抛出异常后，raise  后面的代码不再执行，为了能够捕获异常，"except"语句必须要用相同的异常来抛出类对象或者字符串。
# 使用raise主动抛出异常，输入小于5的数就会抛出异常，大于5的数不会抛出异常
# class Func_test():
#     def start(self):
#         try:
#             content=int(input('请输入数字'))
#             if content<5:
#                 raise Exception('你输入的数字小于5')
#         except Exception as info:
#             print(info)
#         else:
#             print('无异常')
# # 将类实例为对象
# func=Func_test()
# # 直接类名调用方法
# Func_test.start(func)

#####使用raise抛出自己定义的异常
# class MyException(Exception):
#     def __init__(self,num,atleast):
#         # 调用父类的__init__()
#         super().__init__()
#         self.num=num
#         self.atleast=atleast
#
# class Func_test():
#     def start(self):
#         try:
#             content=int(input('请输入数据：'))
#             if content<5:
#                 raise MyException(content,3)
#         except Exception as s:
#             print('当前大小是%s，最少的数是%s'%(s.num,s.atleast))
#         else:
#             print('输入的结果符合要求')
# # 将类实例为对象
# t=Func_test()
# # 用类对象调用方法
# t.start()

#####工作中自己定义的一场通常会把所有的异常封装在一个模块中，统一的处理

























