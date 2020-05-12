"""
@File    : 1_在图上显示出注释信息.py
@Time    : 2020/5/8 9:28 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.arange(-10,11,1)

y=x*x

pyplot.plot(x,y)

# 注释信息
pyplot.annotate('this is the bottom',xy=(0,1),xytext=(0,20),arrowprops=dict(facecolor='r',frac=0.5))
'''
参数说明：
xy  注释点的坐标
xytext  注释文字的显示位置坐标
arrowprops  定义箭头样式,默认的是蓝色坐标
facecolor   是箭头颜色
frac        定义箭头上下部分的比例
'''

pyplot.show()












