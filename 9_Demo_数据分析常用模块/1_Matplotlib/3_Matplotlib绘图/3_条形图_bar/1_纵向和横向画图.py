"""
@File    : 1_纵向和横向画图.py
@Time    : 2020/4/23 9:54 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

n=5
y=[20,30,20,25,15]

index=numpy.arange(n)
# 纵向绘图
p1=pyplot.bar(x=index,height=y,align='edge',color='red',width=0.5)

# 横向绘图
p2=pyplot.barh(y=index,width=y,height=0.5,align='edge',color='red')


pyplot.show()






















