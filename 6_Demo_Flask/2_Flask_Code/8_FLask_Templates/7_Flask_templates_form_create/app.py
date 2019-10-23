from flask import Flask
from flask import render_template
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

@app.route('/register')
def register():
    # 把数据库类实例为对象
    form = RegisterForm()
    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
