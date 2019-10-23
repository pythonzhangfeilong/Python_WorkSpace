#####为了充分的利用内存空间以及更有效率的管理内存，变量是有不同类型的
'''
Numbers(数字)I  int(整数)
            I  long(长整型)
            I  float(浮点型)
            I  complex(复数)
布尔类型       True 和False

String(字符串)
List(列表)
Tuple(元组)
Dictionary(字典)
'''

#####在python中只要定义一个变量，而且他有数据，那么他的类型就已经确定了，不需要说明类型，系统会自动的判断

#####使用type()方法可以查看变量的类型

#####变量命名的规则：可以由字母、数字、下划线组成，且数字不能开头，不能与python内的关键字重复

#####查看python中的关键字
# import keyword
# print('python中的关键字有：',keyword.kwlist)

#####变量赋值
'''
1、常规赋值   a=2
2、链式赋值   a=b=2
3、序列解包赋值  name,age='zhang',20
'''

#####python中的垃圾回收机制
'''
当一个常量被生成会占用一份内存，这时有变量指向该常量，那么该常量的引用计数为1，python虚拟机规定，当常量的引用计数为时，该内存地址会被回收
'''

#####使用内置的方法id()查看变量的id
# a=b=2
# print(id(a),id(b))

#####使用内置方法del()可以删除变量
# a=2
# print(a)
# del(a)
# print(a)

#####python是强类型的动态脚本语言

#####在python3中键盘录入的方法是input()










