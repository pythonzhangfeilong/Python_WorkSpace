#####什么是递归函数：函数的内部可以调用其他的函数
# def func1():
#     print('这个是函数一')
# def func2():
#     print('这个是函数二')
# def main():
#     func1()
#     func2()
# main()

#####在函数的内部可以调用其他函数，如果一个函数可以调用自身，那么这个函数就是递归函数，递归函数会形成一个深度循环
# 函数版斐波那契数列
# def feibo(n):
#     a,b=0,1
#     c=[]
#     while n>0:
#         c.append(b)
#         a,b=b,a+b
#         n-=1
#     print(c)
# feibo(10)

# 递归函数版斐波那契数列
# def feibo(n):
#     if n<=1:
#         return n
#     elif n==2:
#         return 1
#     return (feibo(n-1)+feibo(n-2))
# n=int(input('请输入斐波那契个数：>>>'))
# # 生成一个列表
# list_td=[feibo(i) for i in range(1,n+1)]
# # 输出这个列表
# print(list_td)



























