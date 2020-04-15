"""
@File    : 3_显式创建画布_创建多个自定义的直角坐标系.py
@Time    : 2020/4/15 3:08 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
# 创建画布
figure = pyplot.figure()
# 轴1
axes1 = figure.add_subplot(2,1,1)
# 轴2
axes2 = figure.add_subplot(2,1,2)
# 轴1的坐标点
x1=[1,3,5,7]
y1=[4,9,6,8]
axes1.plot(x1,y1)
# 轴2的坐标点
x2=[1,2,4,5]
y2=[8,4,6,2]
axes2.plot(x2,y2)
# 展示画布
figure.show()

# 简便的写法
# axes1.plot([1,3,5,7],[4,9,6,8])
# axes2.plot([1,2,4,5],[8,4,6,2])