from flask import Flask
app = Flask(__name__)

# url规则一：访问链接参数是被一个斜杠分隔
@app.route('/func')
def hello_world():
    return 'Hello World!'

# url规则二：访问链接参数是被俩个斜杠包围
@app.route('/python/')
def func_python():
    return 'This is Python'

if __name__ == '__main__':
    app.run()
