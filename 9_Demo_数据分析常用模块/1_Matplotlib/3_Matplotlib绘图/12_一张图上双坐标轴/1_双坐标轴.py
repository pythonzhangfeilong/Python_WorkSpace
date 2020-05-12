"""
@File    : 1_双坐标轴.py
@Time    : 2020/4/26 4:07 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

def run():
    x=numpy.arange(2,20,1)
    y1=x*x
    y2=numpy.log(x)

    # 画线
    pyplot.plot(x,y1)

    # 添加坐标轴
    pyplot.twinx()

    # 画线
    pyplot.plot(x, y2,color='r')

    # 显示图
    pyplot.show()

run()

















