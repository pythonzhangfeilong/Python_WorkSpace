"""
@File    : 1_坐标图左上角的图例.py
@Time    : 2020/4/26 11:01 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.arange(1,11,1)

# label每条线的名字
pyplot.plot(x,x*2,label='Normal')
pyplot.plot(x,x*3,label='Fast')
pyplot.plot(x,x*4,label='Faster')

# 显示图例 loc用来调整图例的位置，0是自适应，1是右上角，2是左上角，3是左下角，4右下角
# ncol把图例显示为几列
pyplot.legend(loc=0,ncol=3)

pyplot.show()










