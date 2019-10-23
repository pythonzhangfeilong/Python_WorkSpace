#####列表推导式
# list_tuidaoshi=[ i for i in range(10)]
# print(list_tuidaoshi)
# 下面是得到了10以内可以被2整除的数
# list_tuidaoshi=[ i for i in range(10) if i%2==0]
# print(list_tuidaoshi)

#####实战
# L = [[1,2,3],[4,5,6],[7,8,9]]
# # 要求取到1，4，7
# list_tuidaoshi=[L[i][0] for i in range(len(L))]
# print(list_tuidaoshi)
# #要求等到1，5，9
# list_tuidaoshis=[L[i][i] for i in range(len(L))]
# print(list_tuidaoshis)

#####字典推到式
# dict_tuidaoshi={k:v for k,v in {'name':'zhang','age':18}.items()}
# print(dict_tuidaoshi)

#####集合推导式
# set_tuidaoshi={i for i in range(10)}
# print(set_tuidaoshi)

#####元组比较特殊，叫做生成式
tuple_shengchengshi=(i for i in range(10))
for i in  tuple_shengchengshi:
    print(i)










