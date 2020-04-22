"""
@File    : 2_简单的绘图实例.py
@Time    : 2020/4/15 3:31 下午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
from matplotlib import pyplot

# 定义x轴的坐标
x=numpy.arange(1,11)
# 定义y轴的坐标
y=2*x+5
# 坐标图的标题
pyplot.title('Matplotlib Demo')
# x轴的名称
pyplot.xlabel('x axes')
# y轴的名称
pyplot.ylabel('y axes')
# 设置坐标参数
xp=[1,2,3,4]
yp=[7,6,5,4]
# 根据坐标参数绘制
pyplot.plot(xp,yp)
# 展示
pyplot.show()




















