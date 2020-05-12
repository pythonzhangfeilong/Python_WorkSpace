"""
@File    : 1_多个画布也就是多个画布对象.py
@Time    : 2020/4/23 11:58 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot

# 创建画布对象
fig1=pyplot.figure()
ax1=fig1.add_subplot(221)
ax1.plot([1,2,3],[3,2,1])

# 创建画布对象
fig2=pyplot.figure()
ax2=fig2.add_subplot(221)
ax2.plot([1,2,3],[1,2,3])

pyplot.show()