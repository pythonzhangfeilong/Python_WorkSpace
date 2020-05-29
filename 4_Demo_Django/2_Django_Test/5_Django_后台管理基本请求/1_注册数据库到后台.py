#####注册数据库到后台
'''
Django拥有很多在网站开发过程当中需要的通用功能,这些功能被统一的放到了django.contrib下使用这些功能降低了开发者开发的难度，
    提高了开发的效率，这也是django在Python当中相当受欢迎的一大因素，而在django拥有的这些功能当中，让大家最为熟知的就是django的
    后台管理系统，admin。
数据库模型搭建完成后，要给网站进行数据库搭建，并且实现数据库数据库查询，如何实现将数据添加到数据库中，手写是不现实的，所以就有
    了后台，在这里一定要明确后台和后端是分开的

    后端：指出来HTML，css设计的页面之外所有和服务器数据库的交互
    后台：指对网站的数据进行管理的页面和系统，类似在话剧院当中的后台，前台演戏，后台准备管理，
'''

#####Django有自带的后台管理系统admin
'''
    使用后台admin就要查看settings.py中的INSTALLED_APPS里有没有'django.contrib.admin'
        1、确定settings.py文件中的INSTALLED_APPS里有'django.contrib.admin',
        2、确定urls.py中admin的路由没有被注释
            urlpatterns = [
                path('admin/', admin.site.urls),
            ]
        3、创建管理员之前，先要python manage.py migrate先数据库迁移
           然后在pycharm的Terminal这种输入python manage.py createsuperuser创建管理员权限
                Username (leave blank to use 'administrator'): admin
                Email address: 1634025627@qq.com
                Password:123456                     (不会显示出来)
                Password (again):123456             (不会显示出来)
        4、完成上面的操作，启动Django服务，在浏览器的地址中输入http://127.0.0.1:8000/admin/就会访问到admin登陆页
'''



























