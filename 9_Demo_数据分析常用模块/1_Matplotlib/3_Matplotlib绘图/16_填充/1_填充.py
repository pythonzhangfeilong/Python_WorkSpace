"""
@File    : 1_填充.py
@Time    : 2020/5/8 3:27 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.linspace(0.5*numpy.pi,10)

y1=numpy.sin(x)
y2=numpy.sin(2*x)

# 创建对象
fig=pyplot.figure()
# 获取当前的坐标轴
ax=pyplot.gca()

ax.plot(x,y1,color='r')
ax.plot(x,y2,color='b')

# 填充
ax.fill_between(x,y1,y2,where=y1>y2,facecolor='yellow',interpolate=True)
ax.fill_between(x,y1,y2,where=y2>y1,facecolor='green',interpolate=True)
'''
参数说明
where   判断条件
facecolor   背景色
interpolate     自动填充空白区域

'''


# 填充
# pyplot.fill(x,y1,'r',alpha=0.3)
# pyplot.fill(x,y2,'b',alpha=0.3)


pyplot.show()











