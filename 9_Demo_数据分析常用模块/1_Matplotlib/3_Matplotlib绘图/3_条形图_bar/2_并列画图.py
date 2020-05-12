"""
@File    : 2_并列画图.py
@Time    : 2020/4/23 10:19 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

index=numpy.arange(4)

sales_BJ=[52,55,63,53]
sales_SH=[44,66,55,41]

bar_width=0.3

pyplot.bar(x=index,height=sales_BJ,width=0.5,color='b',align='center')
pyplot.bar(x=index+bar_width,height=sales_SH,width=0.5,color='r')

pyplot.show()







