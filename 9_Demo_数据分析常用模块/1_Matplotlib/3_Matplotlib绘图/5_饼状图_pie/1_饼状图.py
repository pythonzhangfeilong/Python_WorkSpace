"""
@File    : 1_饼状图.py
@Time    : 2020/4/23 11:18 上午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot
lables='a','b','c','d'
fraces=[15,30,45,20]

explode=[0,0.05,0,0]

# labels对应的标签
# autopct格式化显示比例
# explode突出显示某一块区域，加的值与上面的数组对应，加的值就是到圆心的距离
# shadow添加阴影
pyplot.pie(x=fraces,labels=lables,autopct='%.f%%',explode=explode,shadow=True)

pyplot.show()










