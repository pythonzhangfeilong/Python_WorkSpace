#####try的嵌套使用
# import time
# try:
#     with open('book.txt','r',encoding='utf-8')as b:
#         try:
#             # 自动打印三行
#             for i in range(3):
#                 print(b.readline())
#                 # 睡2S
#                 time.sleep(2)
#                 # 再读一行
#                 print(b.readline())
#                 # 如果读取到的数据为0，就结束
#                 if len(b.readline())==0:
#                     break
#         finally:
#             b.close()
#             print(b.closed)
# except:
#     print('没有这个文件')

#####捕获异常在函数中的嵌套使用
# def func_one():
#     print('我是函数一')
# def func_two():
#     print('我是函数二')
# def func_san():
#     try:
#         func_one()
#     except Exception as e:
#         # 也可以在出现异常后，在这个下面调用函数
#         print(e)
# func_san()

















