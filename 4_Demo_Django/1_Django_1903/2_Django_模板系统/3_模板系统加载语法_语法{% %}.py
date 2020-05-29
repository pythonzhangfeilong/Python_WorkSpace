#####{%  %} 以大括号和%号包围的  标签语句
'''
    if语句，和python的if逻辑是完全一样，，如果逻辑为真执行if，否则执行else，当然也支持elif语句，并且在HTML语句当中需要
        用{% endif %}来结束判断
'''

# 1、if语句
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
        <p>if语句判断</p>
        {% if name == 'fei' %}
            <p>name is {{ name }}</p>
        {% elif name == 'zhang' %}
            <p style="color: red">name is {{ name }}</p>
        {% endif %}
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            path('index/',views.get_page)                 # 给前端传递参数
        ]
'''

# 2、for循环
'''
    for循环标签语句，如果后端传递到前段是一个可迭代的序列，那么就可以通过循环的方式展示可迭代对象的每一个元素
    
    1、在App文件夹中找到views.py文件写入下面的数据
        News = [
            {"title": "for's editor","author": "for","time": "2018-06-13"},
            {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
            {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
            {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
            {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
            {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
        ]
        def news(request):
            context={'news':News}
            return render(request, 'for.html', context=context)
    2、在templates的文件夹中在for.html的文件中写入下面的数据
        <ul>
            # 循环的是views.py文件中函数context字典值的键（key）
            {% for new in news %}
                {#style="list-style:none;去除标签前面的符号#}
                <li style="list-style:none;">
                    <span>
                        <a href="#">
                            {{ new.title }}
                        </a>
                    </span>
                    &nbsp;&nbsp;&nbsp;&nbsp;<span>{{ new.author }}</span>
                    &nbsp;&nbsp;&nbsp;&nbsp;<span>{{ new.time }}</span>
                </li>
            {% endfor %}
        </ul>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            # path('index/',views.get_page)               # 给前端传递参数的url
            path('for/',views.news)                     # 给前端传递参数的url
        ] 
'''

# 3、嵌套for循环
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        News = [
            {"title": "for's editor","author": "for","time": "2018-06-13"},
            {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
            {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
            {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
            {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
            {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
        ]
        def news(request):
            context={'news':News,'inner':[1,2,3]}
            return render(request, 'for.html', context=context)
    2、在templates的文件夹中在for.html的文件中写入下面的数据
        <ul>
            {% for num in inner %}
                <h1 style="color: red">{{ num }}</h1>
                {% for new in news %}
                    {#style="list-style:none;去除标签前面的符号#}
                    <li style="list-style:none;">
                        <span>
                            <a href="#">
                                {{ new.title }}
                            </a>
                        </span>
                        &nbsp;&nbsp;&nbsp;&nbsp;<span>{{ new.author }}</span>
                        &nbsp;&nbsp;&nbsp;&nbsp;<span>{{ new.time }}</span>
                    </li>
                {% endfor %}
            {% endfor %}
        </ul>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            # path('index/',views.get_page)               # 给前端传递参数的url
            path('for/',views.news)                     # 给前端传递参数的url
        ]
'''
# forloop       （查看for循环的位置）
'''
    它在循环和嵌套循环过程当中起到了指针作用，可以很轻松的看到循环到了哪里，尤其是嵌套循环，forloop给开发者提供了
        类似python脚本的枚举（enumerate）的功能
    1、在App文件夹中找到views.py文件写入下面的数据
        Navigation = [
            {"id": 1, "label": "python", "href": "python", "parent_id": 0},
            {"id": 2, "label": "java", "href": "python", "parent_id": 0},
            {"id": 3, "label": "php", "href": "python", "parent_id": 0},
            {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
            {"id": 5, "label": "django", "href": "python", "parent_id": 1},
            {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
            {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
            {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
            {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
        ]
        def forloop(request):
            context={'data':Navigation}
            return render(request,'forloop.html',context=context)   
    2、在templates的文件夹中在forloop.html的文件中写入下面的数据
        {% for d in data %}
            <p>{{ d.lable }}</p>
            <p>{{ forloop }}</p>
        {% endfor %} 
    3、在项目文件夹中找到urls.py文件写入下面的数据   
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            # path('index/',views.get_page)               # 给前端传递参数的url
            # path('for/',views.news)                     # 给前端传递参数的url
            path('forloop/',views.forloop)              # 给前端传递参数的url
        ]
        
    注意页面输出的结果中：
        Revcounter0:  倒序索引 （到0截止）
        Revcounter:  倒序 （到1截止）
        Parentloop： 父元素的forloop
        Counter: 计数（从1开始）
        Last: 是不是最后一个
        Counter0: 索引计数（从0开始）
        First: 是不是第一个    
'''

# 嵌套for中forloop       （查看for循环的位置）
'''
    1、在App文件夹中找到views.py文件写入下面的数据
        Navigation = [
            {"id": 1, "label": "python", "href": "python", "parent_id": 0},
            {"id": 2, "label": "java", "href": "python", "parent_id": 0},
            {"id": 3, "label": "php", "href": "python", "parent_id": 0},
            {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
            {"id": 5, "label": "django", "href": "python", "parent_id": 1},
            {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
            {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
            {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
            {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
        ]
        def forloop(request):
            context={'data':Navigation,'inner':[1,2,3]}
            return render(request,'forloop.html',context=context)
    2、在templates的文件夹中在forloop.html的文件中写入下面的数据
        {#嵌套forloop#}
        {% for i in inner %}
            {% for d in data %}
                <p>{{ d.lable }}</p>
                <p>{{ forloop }}</p>
            {% endfor %}
        {% endfor %}
            <p>
                注意页面输出的结果中：<br/>
                {#&nbsp;是空格#}
                &nbsp;&nbsp;&nbsp;&nbsp;Revcounter0:  倒序索引 （到0截止）<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Revcounter:  倒序 （到1截止）<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Parentloop： 父元素的forloop<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Counter: 计数（从1开始）<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Last: 是不是最后一个<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;Counter0: 索引计数（从0开始）<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;First: 是不是第一个 <br/>
            </p>
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
            # path('index/',views.index)                  # 模板系统加载的url
            # path('index/',views.get_page)               # 给前端传递参数的url
            # path('for/',views.news)                     # 给前端传递参数的url
            path('forloop/',views.forloop)              # 给前端传递参数的url
        ]
    注意：这个例子侧重的看parentloop部分，这个部分来指出自己的父元素是谁。    
'''












