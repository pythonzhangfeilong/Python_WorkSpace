#####orm数据库映射关系,用于实现面向对象编程语言里不同类型数据库的转换

#####peewee是需要pip insatll peewee

#####peewee支持三种数据库
'''
Mysql
Sqllite
Postgresql
'''

#####peewee连接mysql
import peewee,datetime
# 连接数据库
connect=peewee.MySQLDatabase(database='table_two',host='127.0.0.1',user='root',passwd='')
# 创建一个类，继承peewee.Model创建一个表，peewee创建的时候默认会添加主键ID，创建的数据库默认字段不可为空
class School(peewee.Model):
    name=peewee.CharField(max_length=20,default='None')
    address=peewee.CharField(max_length=20,default='None')
    age=peewee.IntegerField(default='0')
    birthday=peewee.DateTimeField(default=datetime.datetime.now())
    # 将表和数据库连接
    class Mate:
        database=connect
if __name__ == '__main__':
    # 创建表，创建多个表时用[]
    School.create_table()
    # 插入数据
    # s=School.create(name='zhang',age=23,birthday='2019-7-17')
    # s.save()
    # 第二种插入方法
    School.insert(name='小龙女', age=18, birthday='2018-6-12').execute()

    # 更新数据
    # School.update(name = '杨过',age = 10,birthday ='2018-5-10').where(School.id==1).execute()

    # 删除数据
    # s = School.get(name = '杨过')
    # s.delete_instance()
    # 第二种删除数据
    # School.delete_by_id(2)
    # School.delete().where(School.id == 5).execute()

    # 查询语句
    # s = School.select()
    # for i in s:
    #     print(i.name,i.age)

    # s = School.get(School.id == 3)
    # print(s.name,s.age)

    # 有条件的查询
    # s = School.select().where(School.id == 3)
    # for i in s:
    #     print(i.name)

    # 正序查询，倒序查询
    # s = School.select().order_by(School.id.asc())
    # s = School.select().order_by(School.id.desc())
    # for i in s:
    #     print(i.age)






















