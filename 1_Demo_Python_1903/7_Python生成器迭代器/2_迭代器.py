#####什么是迭代器
'''
迭代器是访问可迭代对象的工具
迭代器是指用iter()函数返回的对象
迭代器可以用next()函数获取可迭代对象的数据
迭代器函数iter和next
iter(iterable) 从可迭代对象中返回一个迭代器,iterable 必须是能提供一个迭代器的对象
next(iterator) 从迭代器iterator中获取下一个记录,如果无法获取下一条记录,则触发StopIteration异常
迭代器只能向前取值
用iter函数可以返回一个可迭代对象的迭代器
迭代器对象能用next函数获取下一个元素
'''
# 例
# L=[1,2,3,6]
# c=iter(L)         使用iter()方法将列表对象L变成可迭代对象
# print(next(c))    使用next()方法获取迭代的下一个值
# print(next(c))
# print(next(c))
# print(next(c))

# 常规循环获取列表中的值
# L=[1,2,3,6]
# for i in L:
#     print(i)
# else:
#     print('循环获取结束')

# 使用异常捕捉获取列表中的值
# L=[1,2,3,6]
# c = iter(L)
# try:
#     while True:
#         print(next(c))
# except StopIteration:
#     print('循环获取类表中的值结束')





















