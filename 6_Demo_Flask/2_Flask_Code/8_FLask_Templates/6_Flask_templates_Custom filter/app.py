from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/index')
def func_index():
    data={
        'my_list':[0,1,2,3,4,5,6]
    }
    return render_template('index.html',**data)

# 自定义过滤器，方式一：
def func_buchang(data):
    return data[::2]
# 注册过滤器(第一个参数是过滤器的函数，第二个参数是过滤器的名字)
app.add_template_filter(func_buchang,'buchang')

# 自定义过滤器，方式二
# 注册过滤器
@app.template_filter('buchang3')
# 定义过滤器函数
def func_buchangs(data):
    return data[::3]

if __name__ == '__main__':
    app.run()
