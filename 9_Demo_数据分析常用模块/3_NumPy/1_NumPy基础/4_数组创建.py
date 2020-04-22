"""
@File    : 4_数组创建.py
@Time    : 2020/4/16 11:41 上午
@Author  : FeiLong
@Software: PyCharm
"""
# 一、使用array函数从常规Python列表或元组中创建数组。得到的数组的类型是从Python列表中元素的类型推导出来的。
import numpy
data=numpy.array([2,3,4])
print(data)

# 查看元素类型
print(data.dtype)

datas=numpy.array([1.2, 3.5, 5.1])
print(data.dtype)   # 这里要注意的是，在pycharm中这样输出类型是int64，在Ipython中输出类型是float64,系统命令窗口中输出的类型是float64

# 二、array将序列转换为二维数组
array_1=(1.5,2.3,4)
array_2=(5,6,7)
data_2=numpy.array([array_1,array_2])
print(data_2)

# 三、创建数组时指定数组的类型
data_array=numpy.array([[1,2],[3,4]],dtype=complex)
print(data_array)

# 四、创建数组函数
'''
函数zeros创建一个由0组成的数组，
函数ones创建一个完整的数组，
函数empty创建一个数组，其初始内容是随机的，取决于内存的状态。
默认情况下，创建的数组的dtype是 float64 类型的。
'''

print(numpy.zeros((3,4)))
print(numpy.ones((2,3,4),dtype=numpy.int16))
print(numpy.empty((2,3)))

# 五、为了创建数字组成的数组，NumPy提供了一个类似于range的函数，该函数返回数组而不是列表。
print(numpy.arange(10,30,2))
print(numpy.arange(0,3,0.3))

# 六、当arange与浮点参数一起使用时，由于有限的浮点精度，通常不可能预测所获得的元素的数量。出于这个原因，通常最好使用linspace函数来接收我们想要的元素数量的函数，而不是步长（step）：
from numpy import pi
print(numpy.linspace(0,2,9))
data_s1=numpy.linspace(0,2*pi,100)
print(numpy.sin(data_s1))
















