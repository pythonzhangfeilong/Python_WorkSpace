def func1():
    print("这是函数1")
def func2():
    print("这是函数2")
def main():                 #在底部通过调用main函数，从这开始执行
    print('这个是main函数')
    func1()                 #调用了main函数在执行func1函数
    func2()                 #调用了main函数在执行func2函数
main()                      #开始调用