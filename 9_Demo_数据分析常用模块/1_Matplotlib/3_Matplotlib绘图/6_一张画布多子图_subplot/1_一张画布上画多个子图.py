"""
@File    : 1_一张画布上画多个子图.py
@Time    : 2020/4/23 11:41 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.arange(1,100)

# 创建画布
fig=pyplot.figure()

# 参数一是子图总行数，参数二是子图总列数，参数三是子图位置
ax1=fig.add_subplot(221)
ax1.plot(x,x)

ax2=fig.add_subplot(222)
ax2.plot(x,-x)

ax3=fig.add_subplot(223)
ax3.plot(x,x*x)

ax4=fig.add_subplot(224)
ax4.plot(x,numpy.log(x))

pyplot.show()











