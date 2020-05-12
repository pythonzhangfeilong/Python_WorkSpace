"""
@File    : 8_pyplot 子模块提供 bar() 函数来生成条形图.py
@Time    : 2020/4/15 4:39 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
pyplot.bar(x, y, align =  'center')
pyplot.bar(x2, y2, color =  'g', align =  'center')
pyplot.title('Bar graph')
pyplot.ylabel('Y axis')
pyplot.xlabel('X axis')
pyplot.show()