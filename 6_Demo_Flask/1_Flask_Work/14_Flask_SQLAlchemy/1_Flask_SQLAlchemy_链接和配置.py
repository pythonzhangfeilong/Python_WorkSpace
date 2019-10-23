#####Flask-SQLAlchemy简介：
'''
Flask-SQLAlchemy是Flask的一个扩展，可以实现Flask集成SQLAlchemy，是一个ORM框架。
'''

#####Flask数据库的连接和配置
# 1、SQLAlchemy在使用的时候需要导入：
from flask_sqlalchemy import SQLAlchemy

# 2、Flask连接和配置
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置数据库信息
class Config():
    # 设置数据库链接,mysql就是链接数据库的类型，root是用户名，root：后面跟的是数据库的密码，@后面是数据库的地址信息，后面是数据库名称
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/flask_database/'

    # 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 导入
app.config.from_object(Config)

# 创建数据库对象
db=SQLAlchemy(app)




