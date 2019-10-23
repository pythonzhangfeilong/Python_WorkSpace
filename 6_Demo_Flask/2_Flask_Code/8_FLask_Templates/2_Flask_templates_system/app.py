from flask import Flask
from flask import render_template
app = Flask(__name__)

# 1、{{}}传递字符串
# 传递参数的时候一定不要忘记<参数>
@app.route('/func_one/<user>')
def func_one(user):
    return render_template('hello.html',name=user)

# 2、{% %}语句,注意：传递参数的时候要加<参数>，但是如果传递在html中进行jinjia2语法比较时，还得注意参数的类型
@app.route('/func_two/<int:soure>')
def func_two(soure):
    return render_template('hello.html',mask=soure)

if __name__ == '__main__':
    app.run()
