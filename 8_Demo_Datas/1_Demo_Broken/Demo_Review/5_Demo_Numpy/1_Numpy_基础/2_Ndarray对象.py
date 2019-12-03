"""
创建一个 ndarray 只需调用 NumPy 的 array 函数即可：
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

参数说明：
名称	    描述
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
"""

import numpy
# 1、单维度
np_a=numpy.array([1,2,3])
print(np_a)

# 2、多维度
np_b=numpy.array([[1,2],[3,4]])
print(np_b)

# 3、最小维度
np_c=numpy.array([1,2,3,4,5],ndmin=2)
print(np_c)

# 4、参数
np_d=numpy.array([1,2,3],dtype=complex)
print(np_d)