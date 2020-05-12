"""
@File    : 6_绘制正弦波.py
@Time    : 2020/4/15 4:17 下午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy
import matplotlib
from matplotlib import pyplot

# fname 为你下载的字体库路径，注意 SimHei.ttf 字体的路径
zfont=matplotlib.font_manager.FontProperties(fname="./simhei.ttf")

# 设置x，y轴的参数
x=numpy.arange(0,3*numpy.pi,0.1)
y=numpy.sin(x)

# 设置x，y轴的中文名称和坐标系名称
pyplot.xlabel('x轴',fontproperties=zfont,fontsize=22)
pyplot.ylabel('y轴',fontproperties=zfont,fontsize=22)
pyplot.title('正弦',fontproperties=zfont,fontsize=22)

# 绘制
pyplot.plot(x,y)

# 展示
pyplot.show()