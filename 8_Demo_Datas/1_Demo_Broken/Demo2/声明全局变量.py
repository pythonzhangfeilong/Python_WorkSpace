name='zhang'
def hello():
    global name#声明全局变量
    name=name+' is cool'
    print(name)
hello()