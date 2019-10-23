#####ORM数据库建模_注册
'''
    1、首先就是创建数据库：
        数据库的创建的方式一：
            在cmd窗口下输入：
                mysql -u root -p
                命令解释：
                    mysql使用的前提是电脑配置好了mysql的服务
                    -u 后面跟的是用户名，root是最高权限的用户
                    -p 后面跟的是密码，没有密码就不用写
                    -h 后面跟的是链接地址
            输入创建命令：
                create database dbname charset utf8；
                命令解释：
                    dbname是数据库的名字
                    utf8是数据库的编码
                    其他数据都是固定的格式与内容

        数据库的创建方式二：
            使用Navicat连接创建

    2、然后在项目的根目录下找到settings.py文件，找到DATABASES写入：
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'orm_django',
                'HOST': '127.0.0.1',
                'PROT': '3306',
                'USER': 'root',
                'PASSWORD': '',
            }
        }

    Django的数据库默认是配置是指向sqlite数据库，Django支持的数据库有：
        	postgresql、mysql、oracle、sqlite、SAP SQL Anywhere、IBM DB2、Microsoft SQL Server、Firebird、ODBC
    官方优先推荐PostgreSQL关系数据库。

    3、数据库配置完成之后，接下来就是数据库的同步：
        第一步：检测配置和模型编写是否有误：
            在pycharm的Terminal中输入python manage.py check，出现System check identified no issues (0 silenced).
            就是配置成功，如果出现报错的内容，在项目的根目录__init__.py文件中写入下面的内容，不报错就不要写：
                import pymysql
                pymysql.install_as_MySQLdb()
        第二步：进行数据集语句的生成和数据库操作记录的生成
            在pycharm的Terminal中输入python manage.py makemigrations，执行成功后就会在App的文件夹中的migrations文件夹中
                生成0001_initial.py，在里面包含数据库的操作日志

        第三步：进行数据的同步：
            在pycharm的Terminal中输入python manage.py migrate，执行成功后打开数据库，就会看见很多数据库表，这样就完成
                了功能的注册和数据表的同步
'''

























