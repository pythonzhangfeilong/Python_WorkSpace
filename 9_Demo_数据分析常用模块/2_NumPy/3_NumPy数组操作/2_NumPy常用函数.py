"""
@File    : 2_NumPy常用函数.py
@Time    : 2020/4/22 10:02 上午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
import random
"""
min()   获取最小值
max()   获取最大值
mean()  获取平均值
sort()  排序
"""

# 在1到100之间随机生成10个数
data=numpy.random.randint(1,100,10)
print('随机得到的数据是',data)
print('随机得到数据的最小的是',min(data))          # numpy省略也不会影响函数的使用
print('随机得到数据的最大的是',numpy.max(data))
print('随机得到数据的平均值是',numpy.mean(data))
print('随机得到数据从小到大排序是',numpy.sort(data)) # 排序列外，必须使用numpy
print('随机得到的数据类型是',type(data))

# 随机生成一个6位数
datas=numpy.random.randint(100000,999999,1)[0]
print(datas)















