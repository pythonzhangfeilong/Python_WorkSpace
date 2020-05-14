"""
@File    : 2_画饼状图显示不出中文的处理方法.py
@Time    : 2020/5/13 4:22 下午
@Author  : FeiLong
@Software: PyCharm
"""
# 1、首先根据下面的代码找到fonts文件夹
from matplotlib import pyplot
import matplotlib
print(matplotlib.matplotlib_fname())#输出/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc

# 2、找到ttf文件夹放入下载好的simhei.ttf

# 3、运行下面的代码，重新加载字体库
from matplotlib.font_manager import _rebuild
_rebuild()

# 4、在画图的上方添加下面的代码即可
pyplot.rcParams['font.sans-serif'] = ['SimHei']