#####类方法
'''
类方法是类对象所拥有的方法,需要用修饰器@classmethod来标识其为类方法
对于类方法，第一个参数接受的必须是类对象，一般以cls作为一个参数
访问类方法，能够通过类的实例对象和类的内置方法去访问
'''
# class People():
#     # 类属性
#     country='china'
#     # 类方法，用@classmethod来修饰
#     @classmethod
#     def getCounntry(cls):
#         return cls.country
# # 将类实例为类对象
# p=People()
# # 通过类对象访问类方法
# print(p.getCounntry())
# # 通过类名去调用类方法
# print(People.getCounntry())

#####使用类方法修改类属性
# class People():
#     # 类属性
#     country='china'
#     # 类方法，用@classmethod来修饰
#     @classmethod
#     def getCounntry(cls):
#         return cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country=country
#
# # 将类实例为类对象
# p=People()
# # 类对象调用类方法
# p.setCountry('janpan')
# # 雷鸣调用类属性
# print(People.country)

#####静态方法@staticmethod,静态方法不需要定义cls参数来接受类对象，他是通过类对象直接调用类属性
# class People():
#     country='chian'
#     @staticmethod
#     def getCountry():
#         print(People.country)
#     def test(self):
#         print(self.country)
#
# # 类名直接访问静态方法
# People.getCountry()
# # 将类实例化为对象
# p=People()
# # 类对象调用静态方法
# p.getCountry()
# # 类对象调用类方法
# p.test()

'''
1、从类方法、实例方法和静态方法的形式就可以得出，类方法的对一个参数是类对象cls，通过cls引用的必定是类对象和方法
2、实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性，也可能是实例属性
3、静态方法@staticmethod中不要额外定义参数，因此静态方法中引用雷属性的话，必须通过类对象来引用

方法类别        语法               描述
类法方法        @classmethod       第一个参数是cls，默认传递
静态方法        @staticmethod      没有默认传递的形参
对象方法        def 方法名         第一个参数是self，默认传递
'''

#####类的私有属性和方法
# 给方法前面加俩个__就是私有方法，类属性同样适用
'''
私有类属性(__age）；
私有实例属性（self.__name）；
私有实例方法（__func()）。
私有的属性和方法只能在类的内部调用不能在外部调用。
'''
#####私有类属性
# class Cat():
#     __age=18
#     def func(self):
#         print(Cat.__age)
# # 将类实例为对像
# tom=Cat()
# # 通过类对象调用方法
# tom.func()
# # 通过类名调用私有类方法(在类的外部调用是会报错的)
# print(Cat.__age)

#####私有实例属性
# class Cat():
#     def __init__(self,name,age):
#         self.__name=name
#         self.age=age
#     def func(self):
#         print(self.__name)
#         print(self.age)
# tom=Cat('zhang',18)
# # 通过类对象调用类方法
# tom.func()
# # 通过类对象调用实例属性
# print(tom.age)
# print(tom.__name)#这个是属于在类的外部调用私有实例属性，所以会报错

#####私有实例方法
# class Cat():
#     def __func(self):
#         print('我是实例方法')
#     # 在类的内部调用实例方法
#     def func_diyong(self):
#         print(self.__func())
# # 将类实例为对象
# tom=Cat()
# # 用类对象调用方法
# tom.func_diyong()

'''
根据前面的知识可以得出以下结论：	
如果需要在类外修改类属性，必须通过实例对象去引用然后进行修改。
通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，而不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性

属性叫法	            变量叫法	    描述
类属性（私有和公有）	类变量	    所有对象共享同一份类属性。
实例属性（私/公）	成员变量	    每个不同对象，有不一样值的实例属性

'''








