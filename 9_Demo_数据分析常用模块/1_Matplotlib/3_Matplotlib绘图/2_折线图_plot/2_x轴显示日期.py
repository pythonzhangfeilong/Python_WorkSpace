"""
@File    : 2_x轴显示日期.py
@Time    : 2020/4/23 9:25 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
from matplotlib import dates
import numpy

# converters    日期格式化
date,open,close=numpy.loadtxt('../data.csv',delimiter=',',converters={0:dates.bytespdate2num('%m/%d/%Y')},skiprows=1,usecols=(0,1,4),unpack=True)

# 想要把x轴显示出日期就要使用plot_date()方法，使用此方法后会出现散点图，但是通过linestyle设置会变成折线图
pyplot.plot_date(date,open,linestyle='-',color='red',marker='<')
pyplot.plot_date(date,close,linestyle='-',color='green')


pyplot.show()








