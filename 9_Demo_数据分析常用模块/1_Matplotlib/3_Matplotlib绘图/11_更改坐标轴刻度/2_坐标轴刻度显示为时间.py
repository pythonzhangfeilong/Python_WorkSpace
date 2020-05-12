"""
@File    : 2_坐标轴刻度显示为时间.py
@Time    : 2020/4/26 3:40 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import datetime
import matplotlib
import numpy

def run():
    fig=pyplot.figure()
    start=datetime.datetime(2015,1,1)
    stop=datetime.datetime(2016,1,1)
    # 间隔为1天
    delta=datetime.timedelta(days=1)

    x=matplotlib.dates.drange(start,stop,delta)
    y=numpy.random.randn(len(x))

    # 获取当前坐标
    ax=pyplot.gca()

    # 显示线并且格式化
    ax.plot_date(x,y,linestyle='-',marker='')

    # 让坐标轴刻度自适应
    fig.autofmt_xdate()

    pyplot.show()
run()






