#####xadmin后台样式
'''
    首先xadmin是需要自己安装的，但是pip install xadmin会报错也安装不上
'''
'''
    由于 pip install xadmin安装困难，那么就采用源码直接放在Django项目中,创建新的Python包
        1、在python项目的最外层，创建一个Python包，名为extra_apps,把xadmin放在这个文件夹下
        2、在python项目的最外层，创建一个Python包，名为apps，把项目的App文件夹移动到这个里面
        3、把extra_apps和apps都设置为源文件（在文件夹上右键，移动到Mark Directory as 点击Sources Root）
        4、在settings.py上面部分中加入：
            import os
            import sys
            
            # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
            sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))
        5、项目的根目录下配置urls.py，写入：
            import xadmin
            urlpatterns = [
                path('xadmin/', xadmin.site.urls),
            ]
        6、注册app前要先安装一个pip install django-crispy-forms
        7、然后注册app，把xadmin和crspy_forms的添加到settings.py文件的INSTALLED_APPS下面
        8、重新生成数据库之前要安装
            pip install django-formtools
            pip install httplib2
            pip install django-import_export
        9、重新生成一下数据库
            python manage.py makemigrations
            python manage.py migrate
        10、启动Django项目访问http://127.0.0.1:8000/xadmin/
        11、在App文件夹下创建一个adminx.py文件写入：
        from xadmin import views
        import xadmin
        # 创建xadmin的最基本管理器配置，并与view绑定
        class BaseSetting():
            # 开启主题功能
            enable_themes=True
            use_bootswatch=True
        # 将基本配置管理与viwe绑定
        xadmin.site.register(views.BaseAdminView,BaseSetting)
'''

#####自定义xadmin后台样式
'''
    在adminx.py下写入
        import xadmin
        from .models import  Example
        class ExampleAdmin(object):
            list_display = ['name','type']
            search_fields = ['name','type']
            list_filter = ['name','type']
        xadmin.site.register(Example,ExampleAdmin)


#####配置全局主题：
        from xadmin import views
        # 创建xadmin的最基本管理器配置，并与view绑定
        class BaseSetting(object):
            # 开启主题功能
            enable_themes = True
            use_bootswatch = True
        # 将基本配置管理与view绑定
        xadmin.site.register(views.BaseAdminView,BaseSetting)


#####配置后台说明
    # 全局修改，固定写法
    class GlobalSettings():
        # 修改title
        site_title = 'FOR后台管理界面'
        # 修改footer
        site_footer = 'FOR的公司'
        # 收起菜单
        menu_style = 'accordion'
    # 将title和footer信息进行注册
    xadmin.site.register(views.CommAdminView,GlobalSettings)

#####把App的名字在后台管理中显示中文名
    在App的文件夹中找到apps.py文件，写入：
        from django.apps import AppConfig
        class StayleAppConfig(AppConfig):
            name = 'apps.Stayle_App'
            verbose_name='文章'
    在App的文件夹中的__init__.py写入：
        default_app_config='Stayle_App.apps.StayleAppConfig'


'''












