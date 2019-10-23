#####Python常见的错误:语法错误和异常

#####异常：
'''
由于逻辑或者语法导致程序中断的叫做异常
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行
一般情况下，在python无法正常处理程序就会发生一个异常
异常是python对象，表示一个错误
当python脚本发生异常时需要捕获并且处理，否则程序会终止执行
'''

#####语法格式
'''
try:
    可能触发异常的语句块
except 异常:
    发生指定异常执行的代码
except Exception as e:
    捕获异常，并且给异常命名
except:
    捕获一切异常
else:
    没有异常时执行的代码
fianlly：
    有没有异常都会执行的代码
'''

#####语法错误
# def func()
#     print(a)
'''
SyntaxError: invalid syntax
'''

#####异常
print(a)
'''
NameError: name 'a' is not defined
'''


















