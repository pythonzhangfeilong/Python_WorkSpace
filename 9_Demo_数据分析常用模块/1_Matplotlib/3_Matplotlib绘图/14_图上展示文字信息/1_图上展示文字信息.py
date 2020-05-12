"""
@File    : 1_图上展示文字信息.py
@Time    : 2020/5/8 9:48 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
import numpy

x=numpy.arange(-10,11,1)

y=x*x

pyplot.plot(x,y)

pyplot.text(-2,40,'function:y=x*x',family='serif',size=20,color='r',style='italic',weight=20,bbox=dict(facecolor='r',alpha=0.2))
pyplot.text(-2,20,'function:y=x*x',family='fantasy',size=20,color='g',style='oblique',weight=20)

'''
参数说明：
第一个参数是横坐标
第二个参数是纵坐标
第三个参数是文字内容
family  字体
size    字体大小
color   颜色
style   样式
weight  粗细
bbox    背景
alpha   透明度
'''

pyplot.show()













