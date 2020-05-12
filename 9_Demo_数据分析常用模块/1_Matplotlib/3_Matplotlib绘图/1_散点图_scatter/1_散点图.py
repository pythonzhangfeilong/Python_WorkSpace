"""
@File    : 1_散点图.py
@Time    : 2020/4/22 11:01 上午
@Author  : FeiLong
@Software: PyCharm
"""

import numpy
import random
from matplotlib import pyplot

hight=[]
for i in range(6):
    s=random.randint(100,199)
    hight.append(s)
weight=[]
for i in range(6):
    y=random.randint(30,99)
    weight.append(y)

pyplot.scatter(hight,weight)

pyplot.show()







