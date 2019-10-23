##### Flask HTTP方法
'''
1、Http协议是万维网中数据通信的基础。在该协议中定义了从指定URL检索数据的不同方法。

2、常用的HTTP方法：
    GET         以未加密的形式将数据发送到服务器。最常见的方法。
    POST        用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。
    HEAD        和GET方法相同，但没有响应体。
    PUT         用上传的内容替换目标资源的所有当前表示。
    DELETE      删除由URL给出的目标资源的所有当前表示。

3、默认情况下，Flask路由响应GET请求。但是，可以通过为route()装饰器提供方法参数来更改此首选项。
'''

##### Flask中的POST请求
'''
1、首先创建一个Flask项目，找到粉色的templates文件夹，创建一个login.html，写入
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>login</title>
</head>
<body>
    <form action="http://127.0.0.1:5000/login" method="post">
        <p>Enter name:</p>
        <p><input type="text" name="username"></p>
        <p><input type="submit" value="提交"></p>
    </form>
</body>
</html>
'''

'''
2、在app.py中写入：
from flask import Flask
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
app = Flask(__name__)

@app.route('/success/<name>')
def func_success(name):
    return 'Hello %s!'%name

@app.route('/login',methods=['POST','GET'])
def func_login():
    if request.method=='POST':
        user=request.form['username']
        return redirect(url_for('success',name=user))
    else:
        user=request.form['username']
        return redirect(url_for('success',name=user))

if __name__ == '__main__':
    app.run()
'''















