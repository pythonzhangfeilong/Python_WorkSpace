#####富文本编辑器
'''
1、models.py中插入：
from ckeditor_uploader.fields import RichTextUploadingField
class Article(models.Model):
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    time = models.DateField(verbose_name = "文章发表日期")
    description = RichTextUploadingField(verbose_name = "文章描述")
    content = RichTextUploadingField(verbose_name = "文章内容")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    classify = models.ManyToManyField(Classify)
    #这个图片传送模块 如果 没有default就会出错
    picture = models.ImageField(upload_to = "images/%Y%m",default='image/default.png',verbose_name = "文章图片")
    class Meta:
        verbose_name = '文章'
        verbose_name_plural=verbose_name
    def __str__(self):
        return "文章:%s" % self.title
'''
'''
2、adminx.py中插入：
from django.contrib import admin
from Article.models import *
xadmin.site.register(Article)
class ArticleAdmin(object):
    list_display = ['title','time','description','content','author','classify']
    search_fields = ['title','time','description','content','author','classify']
    list_filter = ['title','time','description','content','author','classify']
'''
'''
3、settings.py中写入
#安装APP功能
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Article',
    'xadmin',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader'
]
#静态路由
STATIC_URL = '/static/'
#静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),
]

#媒体路由,用户上传的数据都在当前的目录下，并且保存
MEDIA_URL = "/media/"
MEDIA_ROOT =  os.path.join(BASE_DIR,"media") 
#静态文件根目录
#STATIC_ROOT = os.path.join(BASE_DIR,"static/ckeditor").replace("\\","/")

#ckeditor上传路径，文件的上传路径，必须配合图形操作文件pillow。必要配置
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_GACKEND = 'pillow'
'''

'''
4、urls.py中写入：
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from Apps.xadmin_App import views
import xadmin
from Apps.xadmin_App.views import *
from django.conf.urls import include, url

from Django_xadmin.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('article$',views.article),
    path('articlelist$',views.articleList),
    path('test/',test,name='test'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
]
'''



