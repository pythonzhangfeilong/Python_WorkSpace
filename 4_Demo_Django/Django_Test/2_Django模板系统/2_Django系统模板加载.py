#####Django模板加载
'''
    模板系统也就是如何加载已存在的HTML，Django项目生成后会自动创建templates文件夹，用来存放HTML模板
    在shettings文件中，TEMPLATES前四行是这样写的：
        TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
    项目的模板要在temolates文件夹下，当然这个文件夹中也有HTML文件

    然后就是开始编写模板加载的视图，在这里要明确，配置模板的目的局势在视图里可以加载到独立的HTML文件中，所以当配置好模板的加载路径
        为了验证其配置成功，要在视图里面编写函数验证一下（也就是写一个HTML的页面响应）

    BASE_DIR 是python 1.6版本后添加的一条配置，目的只有一个，使用python 的os模块动态的获取项目的根目录（manage.py存在的目录的
        绝对路径），这个配置项里用到了os的几个功能：
            1、__file__ python的内置属性，指向脚本本身
            2、os.path.abspath() 获取指定文件的绝对路径
            3、os.path.dirname() 获取当前文件的目录（注意，不是路径，是目录）
    这条配置告诉django项目，项目的模板文件在template目录下，当然，目录下要有HTML文件

    然后开始编写模板加载的视图，在这里必须要确定一件事情，配置模板的目的就是在视图里可以加载到独立的HTML文件，所有当配置好模板加载
        的路径，不管是为了工作还是为了证明配置成功，我们都要到视图里面编写函数来验证。
            模板加载我们分为几个步骤
            1.	加载HTML文件作为模板
            2.	定义后端要传递的参数
            3.	模板加载数据
    这三个步骤亘古不变，只不过有些方法把他们封装了起来，从django最原始的代码看起。
    *****以上内容就是说明了Django配置项目模板的一些过程和原理，实质的就是一个响应HTML文件*****
'''

'''
    以上内容配置完成后，并且在templats文件夹中写好index.html文件，接下来就是配置views.py文件了
    1、在views.py文件中写入：
        from django.shortcuts import render
        from django.shortcuts import HttpResponse
        from django.template.loader import get_template
        from django.template import Context
        
        def get_page(request):
            template=get_template('index.html')
            context=({})
            return HttpResponse(template.render(context))
            
    这段代码当中首先导入了get_template和Context方法，
    get_template方法是用来加载在template目录下的HTML文件的
    Context方法是格式化向前端HTML页面传递的参数的，要注意的是Context需要的参数要是一个字典
    然后在get_page视图函数当中，先用get_template加载了template下的index.html(这个HTML文件需要自己准备)，接着Context定义了
        一个空的字典作为传递到前端的数据，其实就是代表没有数据传递，之后我们返回的内容就是加载了空数据的模板，这样就用django
        最简单的代码实现了加载HTML文件。
    2、在settings文件的第59行插入：'DIRS': [os.path.join(BASE_DIR, "template").replace("\\", "/")]，但是插入这个不能用，就采用原来的
    
    3、在templetas写index.html
    
    4、在urls.py文件中配置路由地址
    from App import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('get_page',views.get_page)
    ]
'''


#####以上的内容设置比较复杂，采用自己的使用的就行#####




















