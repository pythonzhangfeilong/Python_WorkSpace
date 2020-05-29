import xadmin
from .models import Author,Article,Classify,Example
#####xadmin自定义显示
class AuthorAdmin(object):
    list_display = ['name','age','gender','email','phone']
    search_fields = ['name','age','gender','email','phone']
    list_filter = ['name','age','gender','email','phone']

class ExampleAdmin(object):
    list_display = ['name','type']
    search_fields = ['name','type']
    list_filter = ['name','type']

class ArticleAdmin(object):
    list_display = ['title','time','description','content','author','classify']
    search_fields = ['title','time','description','content','author','classify']
    list_filter = ['title','time','description','content','author','classify']

class ClassifyAdmin(object):
    list_display = ['label','description']
    search_fields = ['label','description']
    list_filter = ['label','description']

xadmin.site.register(Example,ExampleAdmin)
xadmin.site.register(Author,AuthorAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Classify,ClassifyAdmin)

#####全局主题配置
from xadmin import views
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True
# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

#####修改后台说明
# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = 'FOR后台管理界面'
    # 修改footer
    site_footer = 'FOR的公司'
    # 收起菜单
    menu_style = 'accordion'
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)