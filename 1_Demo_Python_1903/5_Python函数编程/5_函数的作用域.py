#####函数作用域：
'''
L  local局部作用域，本地作用域
E  enclosing嵌套作用域
G  global全局作用域
B  built-in内建作用域
for，if，while这些流程控制不会形成自己的作用域
'''

#####得到所有模块的方法，内建作用域
# import sys
# print(dir(sys))

#####全局变量
# 全局变量name
name = 'while'
def outer():
  # name = 'for'#嵌套作用域
    def inner():
        #本地作用域
        # name = 'django'
        age = 18
        print(name)
        print(age)
    inner()
outer()
























