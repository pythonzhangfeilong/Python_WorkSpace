'''
生成30个随机数，然后分别计算：
1、这30个数字的奇偶性，奇数返回True，偶数返回False
2、这30个数字的2倍
3、这30个数字是否大于10
要求：
用socket分布式部署给三个client来计算，服务端进行数据汇总显示
'''
#####先生成30个随机数并且判断他们的奇偶性

# 导入random（生成随机数模块）
import random

# 利用random模块中的randint方法生成随机整数
randintlist=[random.randint(1,30)for i in range(30)]

# 输出randintlist这个列表
print('这30个随机数是：',randintlist)

for i in randintlist:
    if i%2==1:
        print('%d该数据为奇数，True'%i)
    elif i%2==0:
        print('%d该数据为偶数，False'%i)
    else:
        break

#####这30个数字的2倍
# 导入random模块
# import random
#
# # 利用random模块中的randint方法生成随机的整数
# randomlist=[random.randint(1,30)for i in range(30)]
#
# # 输出randomlist这个列表
# print(randomlist)
#
# 利用循环完成这30个数的2倍
for i in randomlist:
    # 乘以这个数的2倍
    c=i*2
    # 输出
    print(c,end=',')

#####判断这30个数是否大于10
import random

randomlist=[random.randint(1,30)for i in range(30)]

print('这30个随机数是：',randomlist)

for i in randomlist:
    if i<10:
        print('%d小于10'%i)
    elif i>10:
        print('%d大于10'%i)
    else:
        break
























