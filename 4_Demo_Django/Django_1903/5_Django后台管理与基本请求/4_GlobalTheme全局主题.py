#####1、再到models文件写入：
'''
from django.db import models

class Example(models.Model):
    name=models.CharField(max_length=32,verbose_name='作者')
    type=models.CharField(max_length=32,verbose_name='分类')

    class Mate():
        verbose_name='作者'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '作者：%s'%self.name

#作者
class Author(models.Model):
    gender_choice = (
        ('M','Male'),
        ('F','Female'),
    )
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='作者年龄',blank=True,null=True)
    gender = models.CharField(max_length=2,choices=gender_choice,verbose_name='作者姓名',blank=True,null=True)
    email = models.EmailField(verbose_name='作者邮箱',blank=True,null=True)
    phone = models.CharField(max_length=11,verbose_name='作者电话',blank=True,null=True)
    #在admin下展示这个表的中文名字
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
    # isdelete = models.IntegerField
    def __str__(self):
        return '作者:%s'%self.name
#种类表
class Classify(models.Model):
    label = models.CharField(max_length=32,verbose_name='分类标签')
    description = models.TextField(verbose_name='分类描述')

    class Meta:
        verbose_name='分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '标签:%s'%self.label

from ckeditor_uploader.fields import RichTextUploadingField
#文章
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章标题')
    time = models.DateField(verbose_name='文章发表日期')
    description = RichTextUploadingField(verbose_name='文章描述')
    content = RichTextUploadingField(verbose_name='文章内容')
    #外键关联（一对多关系……）
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # isdelete =
    #多对多关系
    classify = models.ManyToManyField(Classify)

    picture = models.ImageField(upload_to='images/%Y%m',default='image/default.png',verbose_name='文章图片')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '文章:%s'%self.title
'''



#####2、找到adminx文件,写入:
'''
import xadmin
from .models import Author,Article,Classify,Example
#xadmin自定义显示
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
# 注册显示内容
# xadmin.site.register(Example,ExampleAdmin)
xadmin.site.register(Author,AuthorAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Classify,ClassifyAdmin)
生成数据库表python manage.py makemigrations
迁移数据库表python manage.py migrate

#3、全局主题配置
from xadmin import views
# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True
# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)


#4、修改后台说明：
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
'''

#####3、把App的名字在后台显示为中文
'''
1、在App文件夹中的apps.py文件中写入
from django.apps import AppConfig
class XadminAppConfig(AppConfig):
    name = 'Apps.xadmin_App'
    verbose_name='文章'
2、在App文件夹下的__init__文件夹中写入：
default_app_config='xadmin_App.apps.XadminAppConfig'
'''


































