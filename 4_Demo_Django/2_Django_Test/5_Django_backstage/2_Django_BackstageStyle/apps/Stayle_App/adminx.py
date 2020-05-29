#####xadmin后台样式
# from xadmin import views
# import xadmin
# # 创建xadmin的最基本管理器配置，并与view绑定
# class BaseSetting():
#     # 开启主题功能
#     enable_themes=True
#     use_bootswatch=True
# # 将基本配置管理与viwe绑定
# xadmin.site.register(views.BaseAdminView,BaseSetting)

#####自定义xadmin后台样式
import xadmin
from .models import  Exaple
class ExampleAdmin():
    list_display = ['name','type']
    search_fields = ['name','type']
    list_filter = ['name','type']
xadmin.site.register(Exaple,ExampleAdmin)

#####配置全局主题
from xadmin import views
import xadmin
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting():
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

#####个人博客，安装模型到后台
from Stayle_App.models import *
xadmin.site.register(Article)
class ExapleAdmin():
    list_display = ['name','type']
    search_fields = ['name','type']
    list_filter = ['name','type']

class ArticleAdminx():
    list_display=['title','time','content','author']
    search_fields=['title','time','content','author']
    list_filter=['title','time','content','author']

class AuthorAdmin():
    list_display = ['name','age','gender','email','phone']
    search_fields = ['name','age','gender','email','phone']
    list_filter = ['name','age','gender','email','phone']

class ClassifyAdmin():
    list_display = ['lable','description']
    search_fields = ['lable','description']
    list_filter = ['lable','description']

xadmin.site.register(Exaple,ExapleAdmin)
xadmin.site.register(Author,AuthorAdmin)
xadmin.site.register(Article,ArticleAdminx)
xadmin.site.register(Classify,ClassifyAdmin)
