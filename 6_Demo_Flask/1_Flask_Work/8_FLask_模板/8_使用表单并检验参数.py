#####使用表单并检验参数
# 1、在app.py中写入：
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
# 创建数据库表单需要pip install flask_wtf并且导入FlaskForm
from flask_wtf import FlaskForm
# 创建字段
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
# 验证字段
from wtforms.validators import DataRequired
from wtforms.validators import EqualTo

app = Flask(__name__)

# csrf_token伪造，值是随便输入的
app.config['SECRET_KEY']='WE5W6E5F1WE651F6W1EF65WE1F6W1E5F6WE'

# 定义表单的模型类，固定继承FlaskForm
class RegisterForm(FlaskForm):
    """自定义注册表单模型"""
    # 字符串的前面加上u是显示中文名，lable是名字，validators是验证器，DataRequired保证数据必须填写不能为空，DataRequired后面括号中是字段检验的提示信息
    user_name=StringField(label=u'用户名',validators=[DataRequired(u'用户名不能为空')])
    password=PasswordField(label=u'密码',validators=[DataRequired(u'密码不能为空')])
    passwords=PasswordField(
        label=u'确认密码',
        validators=[DataRequired(u'确认密码不能为空'),
        EqualTo('password',u'俩次输入的密码不一致')]
    )
    submit=SubmitField()

@app.route('/register',methods=['POST','GET'])
def register():
    # 把数据库类实例为对象
    form = RegisterForm()

    # 判断form对象数据是否合理,如果是合理的就返回True，如果是不合理的就返回False
    if form.validate_on_submit():
        # 如果没有走这里面的逻辑，就有可能是html中没有添加 {{ form.csrf_token }}
        # 表示验证合格
        # 提取数据
        uname=form.user_name.data
        pwd=form.password.data
        pwds=form.passwords.data
        print(uname,pwd,pwds)

        session['user_name']=uname

        # 跳转页
        return redirect(url_for('func_index'))

    return render_template('register.html',form=form)

# 设置跳转页
@app.route('/index')
def func_index():
    user_name=session.get('user_name','')
    return 'hello %s'%user_name
if __name__ == '__main__':
    app.run(debug=True)

# 2、在templates文件夹中，创建register.html，写入：
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>register</title>
</head>
<body>
    <form action="/register" method="post">
        {{ form.csrf_token }}

        {{ form.user_name.label }}
        <p>{{ form.user_name }}</p>
        {% for data in form.user_name.errors %}
            <p>{{ data }}</p>
        {% endfor %}

        {{ form.password.label }}
        <p>{{ form.password }}</p>
        {% for data in form.password.errors %}
            <p>{{ data }}</p>
        {% endfor %}

        {{ form.passwords.label }}
        <p>{{ form.passwords }}</p>
        {% for data in form.passwords.errors %}
            <p>{{ data }}</p>
        {% endfor %}

        {{ form.submit }}
    </form>
</body>
</html>
'''