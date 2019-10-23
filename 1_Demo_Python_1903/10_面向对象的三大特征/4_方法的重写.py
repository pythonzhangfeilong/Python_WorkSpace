#####重写：python中方法的重写，就是子类中有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
# class Dog():
#     def print_inif(self):
#         print('this is dogclass')
# class Dog_two(Dog):
#     def print_inif(self):
#         print('this is dog_twoclass')
# d=Dog_two()
# d.print_inif()

#####调用父类的方法
'''
固定的写法：
1、super(子类名,self).方法名(参数)
2、super().方法名(参数)
3、父类名.方法名(self,参数)

有参数就传参，没参数就空着
'''
# 想要在重写的时候调用父类的方法，那么据使用父类名点上方法就行了，super慎用
# class Dog():
#     def __init__(self,name):
#         self.name=name
#         self.color='yellow'
# class Cat(Dog):
#     def __init__(self,name):
#         # 父类调用父类的方法
#         Dog.__init__(self,name)
#     def getinit(self):
#         print(self.name)
# tom=Cat('zhang')
# tom.getinit()




















