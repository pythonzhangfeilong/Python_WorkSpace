##### migrate拓展使用介绍：
'''
    1、migtate的使用是需要先安装：
    pip install flask_script
    pip install flask_migrate

    2、然后在项目中导入使用
    from flask_script import Manager    # 用命令操作的扩展包
    from flask_migrate import Migrate,MigrateCommand  # 操作数据库迁移文件的扩展包

    3、创建FLask脚本管理对象
    manager = Manager(app)

    4、创建数据库迁移工具对象
    migrate=Migrate(app,db)

    5、向migrate对象中添加数据库的操作命令
    manager.add_command('db',MigrateCommand)

    6、通过manager对象启动程序
    if __name__ == '__main__':
        manager.run()
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 1、导入命令操作的拓展包和操作数据库迁移文件的拓展包
from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

app = Flask(__name__)
# 2、创建FLask脚本管理对象
manager=Manager(app)

# 配置数据库信息
class Config():
    # 设置数据库链接，mysql是连接数据库的类型，root是用户名，root:后面跟的是数据库的密码，@后面是数据库的地址信息，/后面是数据库的名称
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost/flask_three"
    # 动态追踪数据库的修改，性能不好，且未来的版本中会消除，目前只是为了解决控制台的提示才是这样写的
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# 导入数据库
app.config.from_object(Config)


# 创建数据库对象
db=SQLAlchemy(app)

# 3、创建数据库迁移工具对象
migrate=Migrate(app,db)

# 4、向migrate对象中添加数据库的操作命令
manager.add_command('db',MigrateCommand)

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
    email = db.Column(db.String(64))
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
    # 通过manager对象启动程序
    manager.run()

#####Flask执行同步数据库操作
'''
1、创建迁移仓库migrations文件夹
在pycharm的Terminal中执行python create_migrations.py db init，在项目文件夹中生成migrations文件夹
2、在迁移仓库migrations文件夹中创建version文件，里面存放数据库记录
在pycharm的Terminal中执行python create_migrations.py db migrate，这个操作和Django中的python manage.py makemigrations一样
注意：生成数据库记录的时候还可以在后面添加-m '创建时描述信息' python create_migrations.py db migrate -m '首次创建'
3、将数据库记录文件同步到数据库中
在pycharm的Terminal中执行python create_migrations.py db upgrade，这个操作和Django中的python manage.py migrate一样
4、查看历史操作信息(前提是在操作的时候加了python create_migrations.py db migrate -m '。。。')
在pycharm的Terminal中执行python create_migrations.py db history 
5、回退到上一步
在pycharm的Terminal中执行python create_migrations.py db downgrade
6、回退到指定的版本
在pycharm的Terminal中执行python create_migrations.py db downgrade 版本编号(版本编号就是查看历史操作信息前面的那一串数字)

'''


