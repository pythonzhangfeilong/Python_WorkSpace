"""
@File    : 4_获取系统已注册字体.py
@Time    : 2020/4/15 3:51 下午
@Author  : FeiLong
@Software: PyCharm
"""
import matplotlib
from matplotlib import pyplot
# 查找出系统注册的字体
a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])

for i in a:
    print(i)

# 打印出你的 font_manager 的 ttflist 中所有注册的名字，找一个看中文字体例如：STFangsong(仿宋）,然后添加以下代码即可：

pyplot.rcParams['font.family']=['STFangsong']
# 苹果笔记本宋体设置
pyplot.rcParams['font.family']=['Songti SC']

