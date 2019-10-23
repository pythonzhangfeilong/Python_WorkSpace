##### context是用来封装要传递给前端的数据
'''
    Django模板系统在前端调用数据主要用到了三种方式
        {{  }} 以双大括号包围的 变量
        {%  %} 以大括号和%号包围的标签语句
        |  用于变量后进行修饰的过滤器
'''

##### 1、{{  }} 以双大括号包围的 变量
# 1、向前端传递参数
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        class Teacher():
            def teacher(self):
                return 'This is class Teacher'
        def get_page(request):
            context={
                'name':'zhang',
                'age':23,
                'project':['Python','Linux','Java'],
                'company':{'name':'Python','address':'huhehaote'},
                # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
                'methde':Teacher()
            }
            return render(request,'index.html',context=context)
            
            在index.html中按照下面的写就是调用类方法
            # {{methde.teacher}}
    2、在templates的文件夹中在index.html的文件中写入下面的数据
        {# 1、向前端传递参数#}
        <p>变量的实例</p>
        {{ name }}<br/>
        {{ age }}<br/>
        {{ progect }}<br/>
        {{ company }}<br/>
        {{ methde.teacher }}
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            path('index/',views.get_page)                 # 给前端传递参数
        ]
'''

# 2、对其中字符串变量进行操作（根据索引取值、格式化）
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        class Teacher():
            def teacher(self):
                return 'This is class Teacher'
        def get_page(request):
            context={
                'name':'zhang',
                'age':23,
                'project':['Python','Linux','Java'],
                'company':{'name':'Python','address':'huhehaote'},
                # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
                # {{methde.teacher}}
                'methde':Teacher()
            }
            return render(request,'index.html',context=context)
    2、在templates的文件夹中在index.html的文件中写入下面的数据
        {#2、前端字符串格式化#}
        <p>直接调用的变量是: {{ name }}</p>
        <p>根据索引取1上的值：{{ name.1 }}</p>
        <p>使用upper将字符串变成大写：{{ name.upper }}</p>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            path('index/',views.get_page)                 # 给前端传递参数
        ]
'''

# 3、对列表进行调用和索引取值
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        class Teacher():
            def teacher(self):
                return 'This is class Teacher'
        def get_page(request):
            context={
                'name':'zhang',
                'age':23,
                'project':['Python','Linux','Java'],
                'company':{'name':'Python','address':'huhehaote'},
                # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
                # {{methde.teacher}}
                'methde':Teacher()
            }
            return render(request,'index.html',context=context)
    2、在templates的文件夹中在index.html的文件中写入下面的数据
        {#3、对列表进行调用和取值#}
        <p>对列表进行调用和取值</p>
        <p>变量是个列表，调用的列表是：{{ project }}</p>
        <p>根据列表的索引取值：{{ project.1 }}</p>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            path('index/',views.get_page)                 # 给前端传递参数
        ]
'''

# 4、对字典进行调用和根据键取字典值
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        class Teacher():
            def teacher(self):
                return 'This is class Teacher'
        def get_page(request):
            context={
                'name':'zhang',
                'age':23,
                'project':['Python','Linux','Java'],
                'company':{'name':'Python','address':'huhehaote'},
                # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
                # {{methde.teacher}}
                'methde':Teacher()
            }
            return render(request,'index.html',context=context)
    2、在templates的文件夹中在index.html的文件中写入下面的数据
        {#4、对字典进行调用和取值#}
        <p>对字典进行调用和取值</p>
        <p>变量是个字典，调用的字典是：{{ company }}</p>
        <p>根据键取的字典值是：{{ company.name }}</p>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            path('index/',views.get_page)                 # 给前端传递参数
        ]
'''












