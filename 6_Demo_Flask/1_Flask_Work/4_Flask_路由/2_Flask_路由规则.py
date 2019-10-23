#####Flask路由规则
'''
Flask的URL规则基于Werkzeug的路由模块,确保形成的URL是唯一的。

Werkzeug是Python的WSGI规范的实用函数库。使用广泛，基于BSD协议.
'''


#url规则一：访问链接参数是被一个斜杠分隔

from flask import Flask
app = Flask(__name__)

@app.route('/func')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
'''
在上面的这个规则中url地址是http://127.0.0.1:5000/func   ，   注意func的后面并没有斜杠   访问成功
如果上面的这个规则中url地址是：http://127.0.0.1:5000/func/， 注意func的后面有斜杠       访问失败Not Found
'''

# url规则二：访问链接参数是被俩个斜杠包围
from flask import Flask
app = Flask(__name__)

@app.route('/python/')
def func_python():
    return 'This is Python'

if __name__ == '__main__':
    app.run()
'''
在上面的这个规则中url地址是http://127.0.0.1:5000/python   ，   注意func的后面并没有斜杠   访问失败Not Found
如果上面的这个规则中url地址是：http://127.0.0.1:5000/func/，   注意func的后面有斜杠       访问成功
'''



















