#####当一个函数拥有多个路由时，都可以直接访问

# 1、在app.py文件中写入下面的内容：
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def func_hello():
    return 'Hello Word!'

if __name__ == '__main__':
    app.run()

# 2、在浏览器访问下面的俩个地址
'''
地址一：http://127.0.0.1:5000
地址二：http://127.0.0.1:5000/index
'''