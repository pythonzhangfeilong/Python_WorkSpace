#####FLask模板
'''
Flask模板可以以HTML的形式返回绑定到某个url的函数输出
'''

# 例：输出一个Hell Word
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

##### 通过render_template()呈现html文件
# 注意：所有的html文件只能创建在templates文件夹中
'''
1、首先在templates文件夹下创建一个first_html.html
'''

'''
2、在app.py中写入下面的内容，在写之前要导入render_template来访问html
'''
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/first_html')
def func_html():
    return render_template('first_html.html')

if __name__ == '__main__':
    app.run()

'''
3、启动Flask服务，在浏览器中访问http://127.0.0.1:5000/first_html
'''
