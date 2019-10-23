#####Flask的cookies
'''
Cookie是以文本文件的形式存放在客户端的计算机上。
    目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。
Request对象包含Cookie的属性。
    它是所有cookie变量及其对应值的字典对象，客户端已传输。除此之外，cookie还存储其网站的到期时间，路径和域名。
在Flask中，对响应对象设置cookie。
    使用make_response()函数从视图函数的返回值获取响应对象。之后，使用响应对象的set_cookie()函数来存储cookie。
读回cookie很容易。
    request.cookies属性的get()方法用于读取cookie。
'''
# 1、首先在templates文件夹中创建一个index.html文件，写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
<html>
   <body>
      <form action = "/setcookie" method = "POST">
         <p><h3>Enter userID</h3></p>
         <p><input type = 'text' name = 'nm'/></p>
         <p><input type = 'submit' value = 'Login'/></p>
      </form>
   </body>
</html>
</body>
</html>
'''

# 2、在app.py文件中写入：
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
   # 注意下面的这种写法可以直接的返回给html并且使用到了字符串拼接
   return "<h1>welcome %s </h1>"%name

# 3、在templats文件夹中创建一个readcookie.html，写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>readcookie</title>
</head>
<body>
    {{ data }}
</body>
</html>
'''

# 4、在浏览器中访问：http://127.0.0.1:5000，提交成功后会跳转到http://127.0.0.1:5000/setcookie展示文件大小以及状态，访问
#    http://127.0.0.1:5000/getcookie会得到Welcome +输入的内容





















