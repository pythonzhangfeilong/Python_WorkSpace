"""
@File    : 7_subplot()在一张图中画多个坐标系.py
@Time    : 2020/4/15 4:29 下午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
import matplotlib
from matplotlib import pyplot

# 计算正弦和余弦曲线上的点，还有x,y的值
x=numpy.arange(0,3*numpy.pi,0.1)
y_sin=numpy.sin(x)
y_cos=numpy.cos(x)

# 激活第一个subplot
pyplot.subplot(2,1,1)
# 绘制第一个图像
pyplot.plot(x,y_sin)
pyplot.title('Sin')

# 如果把第二张图的subplot()改的和第一张图的一致，那么就会把俩张图摞起来

# 激活第二个subplot
pyplot.subplot(2,1,2)
# 绘制第二个图像
pyplot.plot(x,y_cos)
pyplot.title('Cos')

pyplot.show()







