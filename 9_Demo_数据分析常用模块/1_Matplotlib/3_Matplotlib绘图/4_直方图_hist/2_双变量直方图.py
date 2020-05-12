"""
@File    : 2_双变量直方图.py
@Time    : 2020/4/23 11:08 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.random.randn(1000)+2
y=numpy.random.randn(1000)+3

pyplot.hist2d(x,y)

pyplot.show()


