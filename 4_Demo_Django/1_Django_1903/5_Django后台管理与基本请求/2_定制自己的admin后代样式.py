#####Django自带admin后台管理系统,订制自己的样式：
'''
    1、首先确认settings.py文件中的INSTALLED_APPS里面包含'django.contrib.admin'
    2、确认urls.py文件中的urlpatterns里面包含path('admin/', admin.site.urls)
    3、在settings.py中的DATABASES里配置数据库
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'database_two',
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
    7、给后台添加样式需要定义样式类
        list_display = ('id','Name',)     --列表中显示的列
        search_fields = ('id', 'Name')   --搜索框
        list_filter = ('Name',)              --侧边过滤器
        date_hierarchy = 'DataTime3'  --时间下拉
        ordering = ('-DataTime3',)      --列表中的排序
        fields = ('Name','DataTime1')  --详细页面字段顺序
        filter_horizontal = ('Name',)    --显示多对多的关系
        raw_id_fields = ('publisher',)   --显示外键的数据
    8、在models.py中写入：
        class Example(models.Model):
            name=models.CharField(max_length=32,verbose_name='名字')
            type=models.CharField(max_length=32,verbose_name='类型')
    9、在admin.py中写入：
        from Customize_Style_App.models import Example
        @admin.register(Example)
        class ExampleAdmin(admin.ModelAdmin):
            list_display = ('name','type')
            search_fields = ('name','type')
            list_filter = ('name','type')
    10、在浏览器中刷新页面
'''