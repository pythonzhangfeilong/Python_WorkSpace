# # 多条件嵌套
# a='zhangfeilong'
# for i in a:
#     if i=='a':
#         pass
#     elif i=='g':
#         continue
#     else:
#         print(i,end='')
# # while循环语句
# i=1
# while i<10:
#     if i==5:
#         pass
#     else:
#         print(i,end='')
#     i+=1
# # 列表推到式
# a= [i for i in range(10)]
# print(a)
# # 字典推到式
# a={k:v for k,v in {'name':'zhang','age':20}.items()}
# print(a)
# # 集合推到式
# a=(1,2,3,4,5)
# b= {i for i in a}
# print(b)
# 元组生成式
a=(i for i in range(5))
for i in a:
    print(i)