"""
@File    : 1_网格.py
@Time    : 2020/4/26 10:44 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

# 生成一个数组
y=numpy.arange(5)

# 绘制图
pyplot.plot(y,y*2)

# 显示网格
pyplot.grid(True)

# 显示画面
pyplot.show()













