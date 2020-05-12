"""
@File    : 1_直方图.py
@Time    : 2020/4/23 10:41 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

m=100
s=20

x=m+s*numpy.random.randn(200000)

# bins图中有几个直方    默认边框是没有颜色的，加上edgecolor边框就会有颜色   density=False是否生成概率密度函数
pyplot.hist(x,bins=1000,color='red',edgecolor='black')

pyplot.show()
