"""
@File    : 2_隐式创建画布_创建一个使用默认的直角坐标系.py
@Time    : 2020/4/15 3:00 下午
@Author  : FeiLong
@Software: PyCharm
"""
import matplotlib
from matplotlib import pyplot

x=[1,3,5,7]
y=[4,9,6,8]

# 上下一一对应，表示为x，y坐标为(1,4)(3,9)(5,6)(7,8)
pyplot.plot(x,y)

pyplot.show()