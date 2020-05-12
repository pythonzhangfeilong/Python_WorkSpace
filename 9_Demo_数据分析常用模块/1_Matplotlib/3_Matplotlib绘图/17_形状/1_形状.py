"""
@File    : 1_形状.py
@Time    : 2020/5/11 10:54 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
from matplotlib import patches
import numpy

def run():
    fig=pyplot.figure()
    ax=fig.add_subplot(111)
    xy1=numpy.array([0.2,0.2])
    # 长方形位置是用左下角确定的
    xy2=numpy.array([0.2,0.8])
    xy3=numpy.array([0.8,0.2])
    xy4=numpy.array([0.8,0.8])

    # 圆形，生成画图片的对象，第一个参数是圆心位置，第二个参数是半径
    circle=patches.Circle(xy1,0.05)
    ax.add_patch(circle)

    # 长方形,生成画图片的对象，第一个参数是厂房形左下角的位置，第二个参数是宽，第三个参数是高
    rect=patches.Rectangle(xy2,0.2,0.1,color='r')
    ax.add_patch(rect)

    # 多边形，生成画图片的对象，第一个参数是多边形中心的位置，第二个参数是多边形的边数，第三个参数是多边形各顶点到中心的距离
    polygon=patches.RegularPolygon(xy3,5,0.1,color='g')
    ax.add_patch(polygon)

    # 椭圆形，生成画图片的对象，第一个参数是椭圆形中心的位置，第二个参数是长轴的长度，第三个参数是短轴的长度
    ellipes=patches.Ellipse(xy4,0.4,0.2,color='y')
    ax.add_patch(ellipes)

    # 由于坐标轴中比例不正确，所以加这一句显示原型
    ax.axis('equal')

    # 添加网格
    pyplot.grid()

    pyplot.show()

run()


















