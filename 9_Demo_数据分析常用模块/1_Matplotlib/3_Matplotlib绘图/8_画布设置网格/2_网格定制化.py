"""
@File    : 2_网格定制化.py
@Time    : 2020/4/26 10:49 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

y=numpy.arange(5)

pyplot.plot(y,y*2)

# color颜色   linewidth宽度     linestyle线条
pyplot.grid(color='r',linewidth='2',linestyle='--')

pyplot.show()