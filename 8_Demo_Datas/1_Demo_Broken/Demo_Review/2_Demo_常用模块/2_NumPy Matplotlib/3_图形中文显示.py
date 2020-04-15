"""
@File    : 3_图形中文显示.py
@Time    : 2020/4/15 3:40 下午
@Author  : FeiLong
@Software: PyCharm
"""
import matplotlib
import numpy
from matplotlib import pyplot

# 首先下载字体https://www.fontpalace.com/font-details/SimHei/

# fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
zfont=matplotlib.font_manager.FontProperties(fname="./simhei.ttf")

x = numpy.arange(1,11)
y =2*x+5
pyplot.title("Matplotlib - 测试", fontproperties=zfont,fontsize=22)

# fontproperties 设置中文显示，fontsize 设置字体大小
pyplot.xlabel("x 轴", fontproperties=zfont,fontsize=22)
pyplot.ylabel("y 轴", fontproperties=zfont,fontsize=22)
pyplot.plot(x,y)
pyplot.show()










