#####Flask_静态文件
'''
    Web项目开发过程中通常会使用到静态文件，例如CSS、JavaScript、image，这些文件固定的存放在创建项目时包含的static文件夹中
'''
# 1、首先在templates文件夹中创建一个index.html文件，写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
    <script type="text/javascript" src="/static/JavaScript.js"></script>
</head>
<body>
    <input type="button" onclick="sayHello()" value="Say Hello">
</body>
</html>
'''

# 2、在项目自带文件夹static中，创建Javascript文件夹，写入：
'''
function sayHello() {
    alert('Hello Word!')
}
'''

# 注意：在Flask中给绑定函数的url地址为/时，在浏览器访问127.0.0.1:5000就会找到这个函数，也就是不加拼接路径

# 3、在app.py文件中写入：
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# 4、启动Flask服务，在浏览器中访问http://127.0.0.1:5000/





