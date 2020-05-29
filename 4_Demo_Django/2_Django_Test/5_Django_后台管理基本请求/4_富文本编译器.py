#####富文本编辑器ckeditor
'''
富文本编辑器安装：pip install django-ckeditor
Django的分页插件：pip install django-pure-pagination
'''

#####个人博客
'''
1、在models.py中写：
    from django.db import models

class Exaple(models.Model):
    # 创建表的时候一定要注意后面不能加逗号
    name = models.CharField(max_length=32, verbose_name='案例的名称')
    type = models.CharField(max_length=32, verbose_name='案例的类型')

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

#文章
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章标题')
    time = models.DateField(verbose_name='文章发表日期')
    description = models.TextField(verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    #外键关联（一对多关系……）
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    #多对多关系
    classify = models.ManyToManyField(Classify)
    # 图片传送模块，如果不写default就会报错
    picture=models.ImageField(upload_to='images',default='image/default')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '文章:%s'%self.title
'''

'''
2、在xadmin中写：
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

'''

'''
3、在settings.py的INSTALLED_APPS中写：
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Stayle_App.apps.StayleAppConfig',
    'xadmin',
    'crispy_forms',
    'ckeditor_uploader',
]
'''

'''
4、创建static文件夹
'''

'''
5、在settings.py的末尾加入
# 静态路由
STATIC_URL = '/static/'
# 静态文件目录
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

#媒体路由,用户上传的数据都在当前的目录下
MEDIA_URL = "/media/"
MEDIA_ROOT =  os.path.join(BASE_DIR,"media")
#静态文件根目录
#STATIC_ROOT = os.path.join(BASE_DIR,"static/ckeditor").replace("\\","/")

#ckeditor上传路径，文件的上传路径，必须配合图形操作文件pillow
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_GACKEND = 'pillow'
'''