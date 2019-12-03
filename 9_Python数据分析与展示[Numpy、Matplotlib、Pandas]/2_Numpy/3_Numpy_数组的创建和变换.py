# 1、ndarray数组的创建方法
"""
(1)从python中的元组、列表等类型创建ndarray数组
x=numpy.array(list/tuple)   可以是列表或元组类型
x=numpy.array(list/tuple,dtype=numpy.float32)
当numpy.array()不指定dtype时，Numpy将更具数据情况关联一个dtype类型

(2)使用numpy中函数创建ndarray数组对象，如：arange，ones，zeros等
numpy.arange(n)         类似range函数，返回ndarray类型，元素从0到n-1
numpy.ones(shape)       根据shape生成一个全1数组，shape是元组类型
numpy.zeros(shap)       根据shape生成一个全0数组，shape是元组类型
numpy.full(shape,val)   根据shape生成一个数组，每个元素值都是val
numpy.eye(n)            创建一个正方的n*n单位矩阵，对角线为，其余都为0
numpy.ones_like(a)      根据数组a的形状生成一个全1数组
numpy.zeros_like(a)     根据数组a的形状生成一个全0数组
numpy.full_like(a,val)  根据数组啊的形状生成一个数组，每个元素值都是val

(3)使用numpy中其他函数创建ndarray数组
numpy.linspace()        根据起止数据等间距的填充数据，形成数组
numpy.concatnate()      将俩个或多个数组合成一个新数组

"""
# 2、ndarray数组类型变换
"""
(1)     维度变换
.reshape(shape)     不改变数组元素，返回一个shape形状的数据，原数组不变
.resize(shape)      与.reshape()功能一致，但修改原数组
.swapaxes(ax1,ax2)  将数据n个维度进行调换
.flatten()          对数组进行将维，返回折叠后的一维数组，原数组不变

(2)     ndarray数组向列表的转换
ls=a.tolist()
"""

# 3、创建数据对象实例
"""
In [1]: import numpy                                                                                                                      

In [2]: numpy.arange(10)                                                                                                                  
Out[2]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [3]: numpy                                                                                                                             
Out[3]: <module 'numpy' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/numpy/__init__.py'>

In [4]: numpy.ones((3,6))                                                                                                                 
Out[4]: 
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])

In [5]: numpy.zeros((3,6),dtype=numpy.int32)                                                                                              
Out[5]: 
array([[0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]], dtype=int32)

In [7]: numpy.eye(5)                                                                                                                      
Out[7]: 
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])

In [8]: x=numpy.ones((2,3,4))                                                                                                             

In [9]: print(x)                                                                                                                          
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]

In [10]: x.shape                                                                                                                          
Out[10]: (2, 3, 4)
"""




























