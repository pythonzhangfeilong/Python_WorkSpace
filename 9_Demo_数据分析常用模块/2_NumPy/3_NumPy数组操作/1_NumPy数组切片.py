"""
@File    : 1_NumPy数组切片.py
@Time    : 2020/4/22 9:57 上午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
"""numpy的切片操作与python中的切片操作一致"""

data=numpy.arange(3,20)
# 根据索引取值
print(data[3])

# 根据索引取一段数据
print(data[4:9])

# 根据步长取值
print(data[::2])