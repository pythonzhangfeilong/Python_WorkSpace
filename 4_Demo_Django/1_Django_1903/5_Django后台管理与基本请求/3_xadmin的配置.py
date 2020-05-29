#####xadmin的配置：
'''
    xadmin直接采用pip install xadmin安装会报错

    所以采用将xadmin的源码放在Django中，并且设置为源文件
'''

'''
    1、为了Django项目的创建的App便于管理
        首先创建一个名为Apps和一个Python Package命名为Extra_Apps,并且右键Mark Directory as 
            点击Sources Root设置为源文件
    
    2、在settings.py中配置：
        import sys
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0,os.path.join(BASE_DIR,'Apps'))
        sys.path.insert(0,os.path.join(BASE_DIR,'Extra_Apps'))
    3、在urls.py中配置xadmin
        import xadmin
        urlpatterns = [
            path('xadmin/', xadmin.site.urls),
        ]
    4、把xadmin和'crispy_forms'放在settings.py的INSTALLED_APPS下面
    5、配置数据库
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'django_xadmin_app',
                'HOST': '127.0.0.1',
                'PORT': '3306',
                'USER': 'root',
                'PASSWORD': '',
            }
        }
    6、创建数据库记录python manage.py makemigrations
       迁移数据库python manage.py migrate
    7、创建后台管理员账号
        python manage.py createsuperuser
    8、在settings.py中，按照下面的修改的就会在网页端显示中文
        LANGUAGE_CODE = 'zh-hans'
        TIME_ZONE = 'Asia/Shanghai'
    
    9、启动Django服务，在浏览器的地址栏中输入：http://127.0.0.1:8000/xadmin/
'''

#####自定义xadmin后台样式
'''
    1、在models.py文件夹中写入：
        from django.db import models
        class Example(models.Model):
            name=models.CharField(max_length=32,verbose_name='作者')
            type=models.CharField(max_length=32,verbose_name='分类')
            # 为了让页面中的标题显示为中文
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
            # 为了让页面中的标题显示为中文
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
            # 为了让页面中的标题显示为中文
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
            #多对多关系
            classify = models.ManyToManyField(Classify)
            # 传图片的指定文件夹
            picture = models.ImageField(upload_to='images/%Y%m',default='image/default.png',verbose_name='文章图片')
            # 为了让页面中的标题显示为中文
            class Meta:
                verbose_name = '文章'
                verbose_name_plural = verbose_name
        
            def __str__(self):
                return '文章:%s'%self.title
    2、在App文件夹中创建一个adminx.py写入：
        import xadmin
        from .models import Author,Article,Classify,Example
        # 创建在页面显示的标题
        class AuthorAdmin():
            list_display = ['name','age','gender','email','phone']
            search_fields = ['name','age','gender','email','phone']
            list_filter = ['name','age','gender','email','phone']
        
        class ExampleAdmin():
            list_display = ['name','type']
            search_fields = ['name','type']
            list_filter = ['name','type']
        
        class ArticleAdmin():
            list_display = ['title','time','description','content','author','classify']
            search_fields = ['title','time','description','content','author','classify']
            list_filter = ['title','time','description','content','author','classify']
        
        class ClassifyAdmin():
            list_display = ['label','description']
            search_fields = ['label','description']
            list_filter = ['label','description']
        # 注册
        # xadmin.site.register(Example,ExampleAdmin)
        xadmin.site.register(Author,AuthorAdmin)
        xadmin.site.register(Article,ArticleAdmin)
        xadmin.site.register(Classify,ClassifyAdmin)
    3、在浏览器地址栏中输入http://127.0.0.1:8000/xadmin/
    
    其实上面的操作就是将models中写的数据库的内容注册在adminx中，然后显示在前端网页的操作，adminx
        中的list_display、search_fields、list_filter是固定的写法
'''
    
#####添加后台插件，配置全局主题


    
    
    





















