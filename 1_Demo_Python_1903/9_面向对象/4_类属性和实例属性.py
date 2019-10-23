#####类属性:定义在类内部,并且在实例方法外部的属性
# 通过类名调用类属性
# class Cat():
#     age=18
#     def eat(self):
#         print('猫在吃')
#     def drink(self):
#         print('猫在喝')
# c=Cat()
# print(c.age)
# print(Cat.age)

# 在类的内部方法调用类属性
# class Cat():
#     age=18
#     def eat(self):
#         print('猫在吃')
#     def drink(self):
#         print('猫在喝')
#     def print_info(self):
#          print(self.age)
# c=Cat()
# # 类对象调用类方法
# c.print_info()
# # 类名调用类属性
# print(Cat.age)
# # 类对象调用类属性
# print(c.age)

#####实例属性
# 初始化方法__init__()
'''
1、初始化方法名必须为 '__init__' 不可改变
2、初始化方法会在构造函数创建实例后自动调用.且将实例自身通过第一个参数self 传入 __init__ 方法
3、构造函数的实参将通过__init__方法的参数列表传入到 '__init__' 方法中
4、初始化方法内如果需要return 语句返回,则只能返回None
'''
#作用：对新创建的方法设置属性
# 语法：
'''
class 类名():
    def __init__(self,[参数列表])
        语句块
'''
# class Cat():
#     def __init__(self):
#         print('__init__被调用')
#     def eat(self):
#         print('猫在吃')
#     def drink(self):
#         print('猫在喝')
# # 把类实例为对象
# tom=Cat()

#####在__init__()方法中给类设置默认属性
# class Cat():
#     def __init__(self):
#         self.name='tom'
#         self.age=18
#     def eat(self):
#         print('猫在吃')
#     def drink(self):
#         print('猫在喝')
#     def print_info(self):
#         print('%s的年龄是%d'%(self.name,self.age))
# # 将类实例化为对象
# tom=Cat()
# # 类对象调用方法
# tom.print_info()

#####使用__init__()传参
# class Cat():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print('猫在吃')
#     def drink(self):
#         print('猫在喝')
#     def print_info(self):
#         print('%s的年龄是%d'%(self.name,self.age))
# tom=Cat('tomcat',22)
# # 类对象调用类方法
# tom.print_info()







