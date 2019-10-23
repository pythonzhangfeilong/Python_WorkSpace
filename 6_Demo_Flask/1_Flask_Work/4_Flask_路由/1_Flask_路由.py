#####Flask路由设置：
'''
Flask中的route()装饰器用于将URL绑定到函数。例如：
@app.route('/func')
def hello_world():
    return 'Hello World!'
其实也就是使用@app.route('/func')给下面的函数绑定了一个127.0.0.1:5000/后面接的访问地址参数起了一个名字
'''