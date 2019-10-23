from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


# 配置数据库信息
class Config():
    # 设置数据库链接，mysql是连接数据库的类型，root是用户名，root:后面跟的是数据库的密码，@后面是数据库的地址信息，/后面是数据库的名称
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/flask_two"
    # 动态追踪数据库的修改，性能不好，且未来的版本中会消除，目前只是为了解决控制台的提示才是这样写的
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# 导入数据库
app.config.from_object(Config)


# 创建数据库对象
db=SQLAlchemy(app)


# 创建数据库表，固定继承db.Model
class Role(db.Model):
    """设置数据库表名"""
    __tablename__='roles'

    # 注意：只要是列前面加上Column，就是作为了数据库的一个字
    # 数据库表字段
    # db.Integer设置为整形，primary_key=True作为主键，设置为主键之后会自增，省去了写autoincrement=True自增
    id = db.Column(db.Integer, primary_key=True)
    # db.Column列，db.String(32)设置为字符串格式长度为32，unique=True内容不可以重复，default='Null'默认值是Null
    name = db.Column(db.String(32), unique=True, default='Null')
    # 把角色表和用户表关联前来，可以写也可以不写backref反推角色表
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role:%s' % self.name
class User(db.Model):
    """用户表"""
    # 自定义数据库表名表名
    __tablename__='users'

    # 数据库表字段
    # db.Integer设置为整形，primary_key=True作为主键，设置为主键之后会自增，省去了写autoincrement=True自增
    id = db.Column(db.Integer,primary_key=True)
    # db.Column列，db.String(32)设置为字符串格式长度为32，unique=True内容不可以重复，default='Null'默认值是Null
    name = db.Column(db.String(32),unique=True,default='Null')
    email = db.Column(db.String(32),unique=True,default='Null')
    password = db.Column(db.String(32),default='Null')
    # db.Column列，db.Integer类型，db.ForeignKey("tbl_users.id")外键设置关联
    role_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return 'User:%s'%self.name
if __name__ == '__main__':
    # 清空数据库的历史表数据据，这个是第一次创建数据库的时候使用的，不需要每一次都使用
    db.drop_all()
    # 创建数据库表
    db.create_all()