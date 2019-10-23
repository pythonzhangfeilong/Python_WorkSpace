#####流程控制三兄弟
'''
1、if（判断）
2、for （循环：广度循环）
3、while  （循环：深度循环）
'''

#####嵌套循环:外层循环一次，内层循环一遍
# num=int(input('请输入一个数字：'))
# if num>5:
#     if num<18:
#         print(5<num<18)
# else:
#     print('以上判断完成')
#     if num<30:
#         print(15<num<30)

#####for循环的格式
'''
for 变量 in 可迭代对象：
    print(变量)
'''
# 例一
# num='asdfghjkl'
# for i in num:
#     print(i)

# 例二
# for i in range(10):
#     print(i)

#####每次输出的内容都会自动的换行，不想自动换行的时候只需要在后面加一个end=''即可
# for i in range(10):
#     print(i,end='')

#####特殊的for循环（取的是每一个元素的第一个元素）
# a=[(4,5),(6,7)]
# for i in a:
#     print(i[0])

#####for 循环的序列解包赋值
# a=[(4,5),(6,7)]
# for i,j in a:
#     print('%d 这是i'%i)
#     print('%d 这是j'%j)

#####while循环：指当满足while条件时，就一直循环while语句块，知道不满足
'''
while (条件)：
    满足条件的语句
else：
    不满足条件的语句
'''
# 假设一个条件一直成立，那么就形成了死循环，python中死循环的条件式while True

#####流程控制词
'''
pass 只进行占位，不做其他处理
break 结束所有循环
continue 结束当前循环
'''




