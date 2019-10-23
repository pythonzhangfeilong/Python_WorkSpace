from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置数据库信息
class Config():
    # 设置数据库链接,mysql就是链接数据库的类型，root是用户名，root：后面跟的是数据库的密码，@后面是数据库的地址信息，后面是数据库名称
    SQLALCHEMY_DATABASE_URL='mysql://root: @127.0.0.1:3306/flask_database/'

    # 跟踪修改，项目数据模型修改,数据库中的模型也会跟着修改
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    # 显示数据库原始查询语句
    SQLALCHEMY_ECHO='True'
# 导入
app.config.from_object(Config)

# 创建数据库对象
db=SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


