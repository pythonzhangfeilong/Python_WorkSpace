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
    users = db.relationship('User', backref="role")

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
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return 'User:%s'%self.name
if __name__ == '__main__':
    # 清空数据库的历史表数据据，这个是第一次创建数据库的时候使用的，不需要每一次都使用
    db.drop_all()
    # 创建数据库表
    db.create_all()

    # 把数据保存到数据库
    # 创建数据库对象role1，并且字段名=要提交到数据库的数据
    role1=Role(name='admin')
    # session对象记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中,添加完数据后一定要记得提交给数据库
    db.session.commit()

    # 创建数据库对象role2，并且字段名=要提交到数据库的数据
    role2=Role(name='zhang')
    # session对象记录对象任务
    db.session.add(role2)
    # 提交任务到数据库中，添加完数据后一定要提交给数据库
    db.session.commit()

    # 一次性添加多条数据到数据库
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=role2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=role2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=role1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=role1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=role2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=role2.id)
    db.session.add_all([us1,us2,us3,us4,us5,us6,us7,us8,us9,us10])
    db.session.commit()