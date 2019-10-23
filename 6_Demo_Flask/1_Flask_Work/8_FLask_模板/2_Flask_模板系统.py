##### Flask模板系统
'''
Web模板系统：web templating system’指的是设计一个HTML脚本，其中可以动态插入变量数据。
web模板系统包括：
    模板引擎（Flask使用jinga2模板引擎）
    某种数据源和模板处理器
Jinja2模板引擎使用以下分隔符从HTML转义。
    {{ ... }}用于表达式可以打印到模板输出
    {% ... %}用于语句
    {# ... #}用于未包含在模板输出中的注释
    # ... ##用于行语句
'''

# 一、{{ }}用于表达式可以打印到模板输出
'''
1、首先在templates文件夹中创建hello.html,写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello</title>
</head>
<body>  
{#1、{{  }}传递字符串#}
    {{ name }}
{#2、{%  %}语句#}
    {% if mask>=60 %}
        <p>你的成绩及格</p>
    {% else %}
        <p>你的成绩不及格</p>
    {% endif %}
</body>
</html>
'''

'''
2、在app.py中写入：
'''
from flask import Flask
from flask import render_template
app = Flask(__name__)

# 传递参数的时候一定不要忘记<参数>
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

'''
3、启动Flask服务，在浏览器地址栏中访问：http://127.0.0.1:5000/hello/zhang
'''