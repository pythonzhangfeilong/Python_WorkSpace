#####按照参数类型分为：位置参数、关键字参数、默认参数、参数组

#####位置参数
# def func(name,age):
#     print('func是位置传参，传入的name是%s'%name)
#     print('func是位置传参，传入的age是%d'%age)
# func('zhang',20)

#####关键字传参
# def func(name,age):
#     print('func是关键字传参，传入的name是%s' % name)
#     print('func是关键字传参，传入的age是%d'%age)
# func(name='zhang',age=20)
# func(age=21,name='fei')

#####默认值传参（默认的参数一定要写在常规参数的后面）
# def func(name,address='呼和浩特市'):
#     print('func是默认值传参，传入的name是%s'%name,'，address是默认的%s'%address)
# func('张飞龙')

#####参数组传参，也叫做不定长传参：*args元组传参，**kwargs字典传参
# def func(*args):
#     print('func是不定长传参中的元组传参，传入的*args是:',args)
# func(1,2,3,4,5,6)

#####字典传参：所有传递的参数都是键值对的形式，键=值
# def func(**kwargs):
#     print('func是不定长传参中的元组传参，传入的**kwargs是:',kwargs)
# func(zhang='fei',age=18)

















