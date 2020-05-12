"""
@File    : 1_生成等差数列折线图.py
@Time    : 2020/4/23 9:14 上午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
from matplotlib import pyplot

# linspace()生成等差数列，把-10到10分成5份
x=numpy.linspace(-10,10,5)
y=x**2

pyplot.plot(x,y)

pyplot.show()










