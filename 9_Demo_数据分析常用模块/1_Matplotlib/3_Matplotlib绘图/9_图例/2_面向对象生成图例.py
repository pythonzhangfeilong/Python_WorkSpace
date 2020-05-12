"""
@File    : 2_面向对象生成图例.py
@Time    : 2020/4/26 11:29 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

def tuli():
    # 创建画布
    fig=pyplot.figure()

    # 创建轴
    axse1=fig.add_subplot(111)

    # 创建x
    x=numpy.arange(1,11,1)

    # 显示线
    pyplot.plot(x,x*2,label='one_xian')

    # 显示图例
    axse1.legend()

    # 显示图
    pyplot.show()

tuli()









