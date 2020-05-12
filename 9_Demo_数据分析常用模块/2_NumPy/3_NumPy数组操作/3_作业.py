"""
@File    : 3_作业.py
@Time    : 2020/4/22 10:19 上午
@Author  : FeiLong
@Software: PyCharm
"""

'''
作业：
    1、使用numpy生成100以内的随机数
    2、将数组存储到文件，再从文件中读取
    3、对数组进行排序、求最大值、最小值、平均值、方差
'''
import numpy
import csv
import codecs
# 在0到100之间随机生成20个数
data=numpy.random.randint(0,100,20)

# 方差
print(numpy.var(data))

# 标准差
print(numpy.std(data))

# 把生成的数据存放到csv文件中
with open('./random_data.csv','w') as ra_work:
    ra_work.write(str(data))

# 读取csv文件中的数组，由于数组存入的时候是以字符串的形式存入的，所以不能够直接读取

csv_file=open('./random_data.csv')    #打开文件
csv_reader_lines = csv.reader(csv_file)    #用csv.reader读文件
date_PyList=[]                        #创建一个空列表
for one_line in csv_reader_lines:
    date_PyList.append(one_line)    #逐行将读到的文件存入python的列表
date_ndarray = numpy.array(date_PyList)    #将python列表转化为ndarray
data_array=numpy.array(date_ndarray[0][0]) #切个片试一下是否成功














