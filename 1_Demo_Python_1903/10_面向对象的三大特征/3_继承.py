#####常规继承
# class Admin():
#     def eat(self):
#         print('吃。。。')
#     def drink(self):
#         print('喝。。。')
# class Dog(Admin):
#     def eat(self):
#         print('狗在吃')
#     def call(self):
#         print('狗在喝')
# class Cat(Admin):
#     def catch(self):
#         print('猫抓老鼠')
#
# # 将类实例为对象
# d=Dog()
# # 使用类对象调用父类的方法
# d.eat()
# tom=Cat()
# tom.eat()
# tom.catch()

#####继承中的私有属性和方法
# class Admin():
#     # 私有实例方法属性
#     def __init__(self,name='汪汪',color='yellow'):
#         self.__name=name
#         self.color=color
#     def eat(self):
#         print('吃。。。')
#     def drink(self):
#         print('喝。。。')
#     # 私有类方法
#     def __test(self):
#         print(self.color)
#     # 方法调用私有实例方法属性
#     def print_info(self):
#         print(self.__name)
# class Dog(Admin):
#     def eat(self):
#         print('狗吃。。。')
#     def call(self):
#         print('汪汪。。。')
# # 把类实例化为对象
# d=Dog()
# # 访问父类的方法
# d.drink()
# print(d.color)

'''
私有的属性、方法，不会被子类继承，也不能被访问
'''

#####多继承：多个子类有同一个父类，并且具有他们的特征
# class Base():
#     def func(self):
#         print('属于Base类')
# class A_class(Base):
#     def func_A(self):
#         print('这个是func_A函数')
# class B_class(Base):
#     def func_B(self):
#         print('这个是func_B函数')
# class C_class(B_class,A_class):
#     pass
# # 将类实例化为对象
# c=C_class()
# # 通过类对象调用父类的方法
# c.func()
# c.func_A()
# c.func_B()
# 查看访问顺序
# print(c.__class__.mro())

#####更改c类中的继承顺序
# class Base():
#     def func(self):
#         print('属于Base类')
# class A_class(Base):
#     def func_A(self):
#         print('这个是func_A函数')
# class B_class(Base):
#     def func_B(self):
#         print('这个是func_B函数')
# class C_class(A_class,B_class):
#     pass
# # 将类实例为对象
# c=C_class()
# print(c.__class__.mro())

'''
说明:
1、python中是可以多继承的并且父类中的方法、属性，子类也会继承
2、python3中多继承遵循mro算法顺序当中的，先广度后深度的原理
3、只会执行一次__init__()文件
'''
'''
总结：
子类在继承的时候，在定义类时，小括号中为父类的类名
子类继承后，父类的属性、方法，都会被继承给子类
私有属性，不能通过对象去直接访问，但是可以通过创建新方法去访问
私有方法，不能通过对象直接访问
私有的属性、方法，不会被子类继承，也不能被访问
'''




























