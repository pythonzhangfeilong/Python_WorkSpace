name='while'#全局变量
def hello():
    name='xiao'#相对于hello（）函数这个是嵌套变量，相对于hi（）是全局变量
    def hi():
        name='zhang'#本地变量
        age='18'
        print(name)
        print(age)
    hi()
hello()