"""
@File    : 2_双坐标轴面向对象的画法.py
@Time    : 2020/4/26 4:44 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy
def run():
    x=numpy.arange(2,10,1)
    y1=x*x
    y2=numpy.log(x)

    fig=pyplot.figure()

    # 创建轴
    ax=fig.add_subplot(111)
    # 画线
    ax.plot(x,y1)
    # 设置轴名称
    ax.set_ylabel('Y1')

    # 设置第二个轴
    ax2=ax.twinx()
    ax2.plot(x,y2,color='red')
    ax2.set_ylabel('Y2')

    ax.set_xlabel('Compare Y1 and Y2')

    pyplot.show()

run()










