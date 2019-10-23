#####Flask URL构建
'''
url_for()函数对于动态构建特定函数的URL非常有用。
该函数接受函数的名称作为第一个参数，以及一个或多个关键字参数，每个参数对应于URL的变量部分
'''
from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

# 注意接收传递参数的时候，要在url后面加上<参数>
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest'%guest

# 注意接收传递参数的时候，要在url后面加上<参数>
@app.route('/user/<name>')
def hello_user(name):
    # 如果名字是admin就会执行hello_admin函数
    if name=='admin':
        return redirect(url_for('hello_admin'))
    # 如果名字不是admin就会执行hello_guest函数，名且把该名字也传递进去
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == '__main__':
    app.run()

'''
hello_user()函数检查接收的参数是否与'admin'匹配。如果匹配，则使用url_for()将应用程序重定向到hello_admin()函数，否则重定向
到将接收的参数作为guest参数传递给它的hello_guest()函数。

在浏览器中访问：http://127.0.0.1:5000/user/admin   符合hello_user()函数的判断          响应的是Hello Admin
在浏览器中访问：http://127.0.0.1:5000/user/zhang   不符合hello_user()函数的判断        响应的是Hello zhang as Guest
'''