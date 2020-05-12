"""
@File    : 1_调整轴范围.py
@Time    : 2020/4/26 11:46 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

def zhou():
    x=numpy.arange(-10,11,1)

    # 画出线
    pyplot.plot(x,x*x)

    '''axis()调整坐标轴范围'''
    print(pyplot.axis())    # 显示的四个参数分别是x轴的最小值、x轴的最大值、y轴的最小值、y轴的最大值
    pyplot.axis([-5,5,20,80])

    '''xlim(),ylim()'''
    pyplot.xlim([-10,11])
    pyplot.ylim([0,100])

    '''xlim(xmin=,xmax=)    ylim(ymin=,ymax=)'''
    pyplot.xlim(xmin=-7,xmax=7)
    pyplot.ylim(ymin=10,ymax=80)

    pyplot.show()
zhou()


