"""
@File    : 1_更改坐标轴刻度.py
@Time    : 2020/4/26 3:28 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

def run():
    x=numpy.arange(1,11,1)

    # 获取当前坐标轴
    ax=pyplot.gca()

    # 把坐标轴分成多少格
    ax.locator_params('x',nbins=20)
    ax.locator_params('y',nbins=10)

    pyplot.plot(x,x)

    pyplot.show()

run()










