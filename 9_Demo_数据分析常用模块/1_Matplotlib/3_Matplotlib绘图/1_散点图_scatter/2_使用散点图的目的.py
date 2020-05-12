"""
@File    : 2_使用散点图的目的.py
@Time    : 2020/4/22 11:20 上午
@Author  : FeiLong
@Software: PyCharm
"""
# 使用散点图的目的就是看数据的相关性，有：正相关、负相关、不相关
import numpy
from matplotlib import pyplot

#####正相关
n=1000
# 生成随机样本
x=numpy.random.randn(n)
y=x+numpy.random.randn(n)*0.5
# s是点的面积大小，c是点的颜色，marker是点的形状，alpha是透明度
pyplot.scatter(x,y,s=20,c='r',marker='>')
pyplot.show()

#####负相关
n=1000
# 生成随机样本
x=numpy.random.randn(n)
y=-x+numpy.random.randn(n)*0.5
pyplot.scatter(x,y)
pyplot.show()


#####不相关
n=1000
# 生成随机样本
x=numpy.random.randn(n)
y=numpy.random.randn(n)
pyplot.scatter(x,y)
pyplot.show()







