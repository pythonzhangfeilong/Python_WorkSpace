#####文件的读取read()
# file_object=open('one_test.txt','r',encoding='utf-8')
# # 使用for循环遍历读取
# for work_hang in file_object:
#     print(work_hang)

#####读取方法
'''
read()会一次性读取全部的文件内容，但是如果文件有10G，程序就会卡死，保险起见可以使用read(size)，每次读取size个字节
readlinse()会每一次读取一行内容
readlinses()会一次性读取所有，按照行返回一个list
'''
# file_object=open('one_test.txt','r',encoding='utf-8')
# 读取全部内容
# print(file_object.read())
# 读取一行内容
# print(file_object.readline())
# # 读取全部内容按照行返回一个list
# print(file_object.readlines())

######写write()
# file_object=open('two_test.txt','w',encoding='utf-8')
# file_object.write('儿子，儿子，我是你爸爸')
# file_object.close()
# print(file_object.closed)

#####写入的方式
'''
1、write()写入的参数是一个字符串，就是写入文件的内容
2、writelinses()写入的参数是一个序列，比如列表，会以迭代的方式写入
'''

#####close()关闭一个已经打开的文件对象，文件关闭后，不能再执行读写操作，如果不关闭文件会一直占内存
# 使用with打开文件就不需要close的操作了，with打开文件默认的在组后添加了close的方法
# try:
#     with open('two_test.txt','r',encoding='utf-8') as file_object:
#         print(file_object.read())
# except Exception as e:
#     print(e)
# finally:
#     print(file_object.closed)

#####with：使用with打开文件就不要在最后加close，因为with默认的执行了close()方法
# with open('two_test.txt','r',encoding='utf-8') as e:
#     print(e.read())
# print(e.closed)

#####对图片进行操作,把图片以二进制的方式打开和写入
# with open('t_girl.jpg','rb') as meinv:
#     with open('t_zoop.jpg','wb') as dongwu:
#         # 动物图片要写入美女图片读取到的数据
#         dongwu.write(meinv.read())

#####指针tell()，返回文件当前指针的位置
# with  open('two_test.txt','r',encoding='utf-8') as e:
#     print(e.tell())

#####seek()用于移动文件指针
'''
语法：
file_object.seek(offset,[whence])
offset移动长度
whence移动位置，0从开头(默认)，1从当前，2从末尾
'''
# with open('one_test.txt','r',encoding='utf-8')as file_object:
#     # 读取一行
#     print(file_object.readline())
#     # 从当前位置移动0个位置
#     file_object.seek(0,0)
#     # 查看指针当前的位置
#     print(file_object.tell())




