from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# 配置数据库信息
class Config():
    # 设置数据库链接,mysql就是链接数据库的类型，root是用户名，root：后面跟的是数据库的密码，@后面是数据库的地址信息，/后面是数据库名称
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/flask_one'

    # 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 导入
app.config.from_object(Config)

# 创建数据库对象
db=SQLAlchemy(app)

# 创建数据库表,固定继承db.Model
class Role(db.Model):
    """用户角色/身份表"""
    # 自定义数据库表名
    __tablename__='tbl_roles'

    # 注意：只要是列前面加上Column，就是作为了数据库的一个字
    # 数据库表字段
    # db.Integer设置为整形，primary_key=True作为主键，设置为主键之后会自增，省去了写autoincrement=True自增
    id = db.Column(db.Integer, primary_key=True)
    # db.Column列，db.String(32)设置为字符串格式长度为32，unique=True内容不可以重复，default='Null'默认值是Null
    name = db.Column(db.String(32), unique=True, default='Null')
    # 把角色表和用户表关联前来，可以写也可以不写backref反推角色表
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role:%s'%self.name


# 创建数据库表,固定继承db.Model
class User(db.Model):
    """用户表"""
    # 自定义数据库表名表名
    __tablename__='tbl_users'

    # 数据库表字段
    # db.Integer设置为整形，primary_key=True作为主键，设置为主键之后会自增，省去了写autoincrement=True自增
    id = db.Column(db.Integer,primary_key=True)
    # db.Column列，db.String(32)设置为字符串格式长度为32，unique=True内容不可以重复，default='Null'默认值是Null
    name = db.Column(db.String(32),unique=True,default='Null')
    email = db.Column(db.String(32),unique=True,default='Null')
    password = db.Column(db.String(32),default='Null')
    # db.Column列，db.Integer类型，db.ForeignKey("tbl_users.id")外键设置关联
    role_id = db.Column(db.Integer,db.ForeignKey("tbl_users.id"))

    def __repr__(self):
        return 'User:%s'%self.name

# 通常在创建表的时候，写法就是直接给类定义一个名字，这样创建的数据库表名就是项目名称_类名
# 自定义数据库表名，在类名的下面写__tablename__=表名前缀




