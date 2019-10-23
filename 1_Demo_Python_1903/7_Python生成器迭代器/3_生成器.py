#####什么是生成器:生成器就是能够动态提供数据的对象,生成器对象也是可迭代对象,生成器就是迭代器的一种

#####生成器有俩种:1、生成器函数  2、生成器表达式

#####生成器：含有yield语句的函数就是生成器函数，此函数被调用就会返回一个生成器的对象

#####生成器表达式：
'''
def 函数()：
    yield
'''

#####说明：
'''
yield用于def函数中，目的是将此函数作用生成器函数使用
yield用来生成数据，共迭代器next(it)函数使用
'''
# def my_func():
#     print('即将生成2')
#     yield 2
#
#     print('即将生成3')
#     yield 3
#
#     print('即将生成4')
#     yield 4
#
#     print('即将生成5')
#     yield 5
#
#     print('即将生成6')
#     yield 6
#
#     print('即将生成7')
#     yield 7
# # 将生成器绑定一个对象
# gen=my_func()
# # 用生成器返回一个迭代器
# it = iter(gen)
# # 利用next()方法中迭代器中获取值
# print(next(it))

#####生成器函数说明：
'''
生成器函数的调用将返回一个生成器的对象，生成器对象是一个可迭代对象
'''

#####生成器表达式
# 语法：(表达式 for 变量 in 可迭代对象 [if 真值表达式])
# if句子可以省略
# 作用：用推导式生成一个新的迭代器
# 例
# yield_list=[i**3 for i in range(5)]
# it=iter(yield_list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

#####练习： 已知有一个列表L，L = [2, 3, 5, 7]，用生成器表达式从此列表中拿到数据,生成列表中数据的平方？
# L = [2, 3, 5, 7]
# yield_L=[i*2 for i in L]
# it=iter(yield_L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

#####zip()函数
# zip(iter1[,iter2[,...]])返回一个zip对象，此对象用于生成元组，此元组的个数由最小的可迭代对象决定
# num=['中国移动','中国联通','中国电信']
# data=['10086','10010','10001']
# 直接输出
# print(list(zip(num,data)))

# for循环输出
# for i in zip(num,data):
#     print(i)

# for序列解包赋值输出
# for x,y in zip(num,data):
#     print(x,'客服电话是：',y)

#####zip()方法的重写
# num=['中国移动','中国联通','中国电信']
# data=['10086','10010','10001']
# def my_zip(iter1,iter2):
#     it1=iter(iter1)
#     it2=iter(iter2)
#     try:
#         while True:
#             a=next(it1)
#             b=next(it2)
#             yield (a,b)
#     except:
#         pass
# for t in my_zip(num,data):
#     print(t)










