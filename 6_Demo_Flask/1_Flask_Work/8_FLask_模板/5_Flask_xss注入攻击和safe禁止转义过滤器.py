'''
1、在app.py中写入：
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/index',methods=['POST','GET'])
def func_index():
    text=''
    如果是post请求，那么就把获取text值传递给text
    if request.method=='POST':
        text=request.form.get('text')
    将text传递给前端
    return render_template('index.html',text=text)
if __name__ == '__main__':
    app.run()
'''

'''
在templates中创建index.html写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    <form action="/index" method="post">
        <textarea name="text" id="" cols="30" rows="10"></textarea>
        <input type="submit" value="提交">
    </form>
    {{ text }}
</body>
</html>
'''

'''
3、启动Flask服务，访问http://127.0.0.1:5000/index
(1)在输入框中，输入<script>alert{'hello word'}</script>
(2)在谷歌浏览器中提交是不会执行<script>alert{'hello word'}</script>，因为谷歌浏览器自动禁止转义
(3)如果是在火狐浏览中提交是会执行<script>alert{'hello word'}</script>，因为火狐浏览器没有禁止转义，这是就需要在
    html中text后面加上过滤器并且加上禁止转移safe，也就是{{ text|safe }}
'''