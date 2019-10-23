from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def func_index():
    return render_template('index.html')

# 表单发布到'/ setcookie' URL。相关联的视图函数设置Cookie名称userID并呈现另一个页面。
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
    # 可以是HTML
    # resp = make_response(render_template('readcookie.html'))
    # 可以是字符串
    resp = make_response('儿子，我是你爸爸')
    print(resp)
    resp.set_cookie('userID', user)
    return render_template('readcookie.html',data=resp)

# 'readcookie.html'包含指向另一个视图函数getcookie()的超链接，它读回并在浏览器中显示Cookie值。
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return "<h1>welcome %s </h1>"%name
