"""
@File    : 1_读取csv文件数据.py
@Time    : 2020/4/22 9:23 上午
@Author  : FeiLong
@Software: PyCharm
"""
import numpy

# 创建csv文件
# with open('各省人口.csv','a') as g:
#     g.close()

# 使用NumPy读取csv文件中的数据
data=numpy.loadtxt('./各省人口.csv',delimiter=',',skiprows=1,usecols=(1,2),unpack=False)
data_dx=data.shape
print(data_dx)  # 这个矩阵有11列，2行
"""
参数解释：
    delimiter   数与数之间是用什么分割的
    skipprows   跳过第几行
    usecols     读取第几列数据
    unpack      把数据分别放在那些变量中
    shape       查看矩阵大小
"""
erling19,erling18=numpy.loadtxt('./各省人口.csv',delimiter=',',skiprows=1,usecols=(1,2),unpack=True)
print(erling19)
print(erling18)








