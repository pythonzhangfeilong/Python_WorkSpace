"""
@File    : 3_面向对象的方式画网格.py
@Time    : 2020/4/26 10:54 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

def wang():
    x=numpy.arange(1,10,1)

    # 创建画布
    fig=pyplot.figure()

    # 创建轴
    axes1=fig.add_subplot(111)

    # x，y坐标值
    pyplot.plot(x,x*2)

    axes1.grid(color='b',linestyle='-.',)

    pyplot.show()

wang()

















