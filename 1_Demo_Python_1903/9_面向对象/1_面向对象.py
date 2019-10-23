'''
对象：万物皆对象，就是事实存在的事物
类： 是对事物的划分，当我们在描述的时候用到类，就是在描述一系列的事物的共性特征,比如：鸟类，我们想要说的是所有鸟的共性比如：卵生，羽毛
实例： 从类当中具体映射出来的个体，比如鸟类当中的鸵鸟

类和实例都有自己独立的内存空间，相互独立互不影响，实例来源于类但是比类更具有个性
'''

'''
域： 属于类或者实例的变量，一些名词，例如name，age……
方法：属于类或者实例的功能(函数)，一般来说是函数。一些动词，吃，喝……
属性: 域和方法的统称
类方法：属于类的功能
类属性：属于类的属性
实例方法：属于实例的功能
实例属性：属于实例的属性
'''

#####面向对象：在编程过程当中，把数据及对数据的操作方法放在一起，作为一个相互依存的整体，用这样的思路编程就是面向对象。
# 在编程过程当中，把数据及对数据的操作方法放在一起，作为一个相互依存的整体，用这样的思路编程就是面向对象。
class Registration():
    def __init__(self):
        self.school={
            'linux':[],
            'Python':[]
        }
    def regster(self,major,student):
        if major in self.school:
            self.school[major].append(student)
            print('报名成功')
        else:
            print('学校没有你想要学习的%s专'%major)
if __name__ == '__main__':
    student={'name':'for','age':18,'gender':'男','major':'Python'}
# 将类实例化为对象
reg=Registration()
reg.regster(student.get('major'),student)
print(reg.school)


















