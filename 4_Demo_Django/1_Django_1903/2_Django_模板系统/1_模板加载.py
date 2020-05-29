##### 1、模板加载过程及注意事项：
'''
    1、使用pycharm创建一个项目后，打开项目的目录中会有一个tenplates粉色的文件夹，这个文件夹用于存放后期在前端展示的HTML文件
    2、确认templates文件夹存在后，打开根目录，找到settings.py文件，查看第55行的TENMPLATES是否是下面的内容
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(BASE_DIR, 'templates')]
                ,
    3、确认TEMPLATES的内容正确之后，再查看settings.py文件的第13和16行，是否是下面的内容
        import os
        # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        BASE_DIR的作用以及其中的含义：
            BASE_DIR 是python 1.6版本后添加的一条配置，目的只有一个，使用python 的os模块动态的获取项目的根目录
            (manage.py存在的目录的绝对路径)，这个配置项里用到了os的几个功能：
                1、__file__ python的内置属性，指向脚本本身
                2、os.path.abspath() 获取指定文件的绝对路径
                3、os.path.dirname() 获取当前文件的目录（注意，不是路径，是目录）
    4、模板加载分为3个步骤：
        1.	加载HTML文件作为模板
        2.	定义后端要传递的参数
        3.	模板加载数据
'''

#####模板加载实例：
'''
    1、首先在templates的文件夹中创建一个index.html的文件
    2、在App文件夹下找到views.py文件，在其中写入下面的内容
        from django.shortcuts import render
        def index(request):
            return render(request,'index.html')
    3、在项目文件夹下找到urls.py文件，在其中添加写入下面的内容，尤其注意导入的内容
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('index/',views.index)
        ]
    4、启动项目,在浏览器的地址栏中输入：http://127.0.0.1:8000/index/
    5、刷新页面就会出现HTML中编写的内容
'''



















