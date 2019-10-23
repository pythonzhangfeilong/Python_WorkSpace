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

    # 定义之后，可以让显示对象的时候更加直观，也Django中的__str__方法的作用一致
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

    # 定义之后，可以让显示对象的时候更加直观，也Django中的__str__方法的作用一致
    def __repr__(self):
        return 'User:%s'%self.name
if __name__ == '__main__':
    #####创建数据库表
    # 清空数据库的历史表数据据，这个是第一次创建数据库的时候使用的，不需要每一次都使用
    db.drop_all()
    # 创建数据库表
    db.create_all()

    ######把数据保存到数据库
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
    # session对象记录对象任务
    db.session.add_all([us1,us2,us3,us4,us5,us6,us7,us8,us9,us10])
    # 提交任务到数据库中，添加完数据后一定要提交给数据库
    db.session.commit()

    #####数据查询
    # 在pycharm中的Terminal中交互时使用from database_select import *
    '''
    查询全部的数据
    Django中查询数据是data=类名.objects.all(),也就是data=User.objects.all()
    Flask中查询数据是data=类名.query.all(),也就是data=User.query.all()
    '''
    # 查询一条数据(data1=类名.query.get(主键值)，也就是下面的这个样)
    data1=User.query.get(1)

    # 有过滤条件filter_by的查询语句(data2=类名.query.查询条件(过滤条件，可以有多个).全部，也就是下面的这个样)
    data2=User.query.filter_by(name='wang',role_id=1).all()

    # 有过滤条件filter_by的查询语句(data3=类名.query.查询条件(过滤条件，可以有多个).第一条，也就是下面的这个样)
    data3 = User.query.filter_by(name='wang').first()

    # filter_by和filter的区别就是查询顾虑条件的时候filter_by是单等号，filter是双等号
    # 有过滤条件filter的查询语句(data4=类名.query.查询条件(过滤条件，可以有多个).全部，也就是下面的这个样)
    data4 = User.query.filter(User.name=='wang', User.role_id==1).all()

    # 过滤条件为或的时候，查询语句(data5=类名.query.查询条件(或(类名.条件,类名.条件)),也就是下面这样)
    # 先导入from sqlalchemy import or_
    from sqlalchemy import or_
    data5=User.query.filter(or_(User.name=='wang',User.email.endswith('163.com')))

    # 复杂条件的查询语句(data6=类名.query.查询条件.跳过几条数据查询返回的结果.查询几条.获取所有数据)
    # 注意offset()是跳过几条数据查询
    data6=User.query.filter().offset().limit().all()

    # 排序查询语句(data7=类名.query.查询条件(类名.排序的字段.排序的方式.获取全部数据))
    data7=User.query.order_by(User.id.desc().all())

    # 分组查询语句
    # 先导入 from sqlalchemy import func
    from sqlalchemy import func
    # data8=数据库对象.session.查询(类名点上分组字段名，func.求和(求和字段).分组(分组字段).获取所有的数据)
    data8=db.session.query(User.role_id,func.count(User.role_id)).group_by(User.role_id).all()

    # 关联查询(data9=类名.查询.获取(编号).关联字段)
    data9=Role.query.get(1).users
    '''
    data9=Role.query.get(1)
    # 查看查询数据的类型
    type(data9)
    # 访问与users字段关联的数据
    data9.users
    '''










