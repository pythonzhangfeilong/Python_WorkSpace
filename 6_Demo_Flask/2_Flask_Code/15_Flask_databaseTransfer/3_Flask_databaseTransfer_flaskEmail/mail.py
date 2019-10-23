from flask import Flask
# pip install flask_mail安装flask_mail并且导入Mail和Message
from flask_mail import Mail,Message
app=Flask(__name__)
# 配置邮件：服务器/端口/传输成安全协议/邮箱名/密码
app.config.update(
    DEBUG=True,
    # 邮箱服务器
    MAIL_SERVER='smtp.qq.com',
    # 端口号
    MAIL_PROT=465,
    # 加密传输
    MAIL_USE_TLS=True,
    MAIL_USERNAME='1634025627@qq.com',
    MAIL_PASSWORD='邮箱授权码'
)

mail=Mail(app)

@app.route('/')
def index():
# sender发送方，recipients接收方,接收方可以是多个
    msg=Message("this is test",sender='1634025627@qq.com',recipients=['1634025627@qq.com','1634025627@qq.com'])
    # 邮件内容
    msg.body="Flask test Mail"
    # 邮件发送
    mail.send(msg)
    print('邮件发送成功')
    return 'mail sucess send'

if __name__ == '__main__':
    app.run()












