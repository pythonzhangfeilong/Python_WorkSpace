#####Django注册数据库到后台
'''
    Django拥有很多在网站开发过程当中需要的通用功能（这些功能被统一的放到了django.contrib下），使用这些功能降低了开发者开发
        的难度，提高了开发的效率，这也是django在Python当中相当受欢迎的一大因素，而在django拥有的这些功能当中，最为熟知的就
        是django的后台管理系统，admin。
'''
'''
    完成数据库模型的搭建，如何将数据添加到数据库中，每一个手写是不现实的，所有Django中提出了后台：
    
    什么是后台什么是后端：
        后端：除HTML、CSS设计的页面之外与服务器数据库的交互
        后台：对网站的数据进行管理的页面和系统
'''

#####Django自带admin后台管理系统
'''
    1、首先确认settings.py文件中的INSTALLED_APPS里面包含'django.contrib.admin'
    2、确认urls.py文件中的urlpatterns里面包含path('admin/', admin.site.urls)
    3、在settings.py中的DATABASES里配置数据库
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'database_one',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD': '',
            }
        }
    4、执行python manage.py makemigrations，在App文件夹中的migratios文件夹中生成数据库表
       执行python manage.py migrate,迁移数据库表
    5、执行python manage.py createsuperuser创建管理员，执行成功后：
        Username (leave blank to use 'administrator'): admin            创建用户名
        Email address: 1634025627@qq.com                                添加邮箱
        Password:                                                       输入密码（不显示）
        Password (again):                                               确认密码（不显示）
        Bypass password validation and create user anyway? [y/N]: y     跳过验证，输入y回车即可
    6、启动Django服务，在浏览器地址栏中访问：http://127.0.0.1:8000/admin，输入用户名和密码即可登陆后台管理系统
'''




















