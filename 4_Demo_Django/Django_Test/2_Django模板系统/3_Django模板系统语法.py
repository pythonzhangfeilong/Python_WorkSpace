#####上一小部分，将HTML文件加载并且发送给前端
'''
    在上一部分的代码中有一个小瑕疵代码里的的context是用来封装要传递给前端的数据，而且如果前端接收有数据，又该怎么使用，来看一下这
        些问题
'''

#####Django模板系统语法
'''
    Django模板系统在前端调用数据主要用到了三种方式:
        {{  }} 以双大括号包围的       变量
        {%  %} 以大括号和%号包围的    标签语句
        |  用于变量后进行修饰的       过滤器
'''

#####{{  }} 以双大括号包围的       变量

# 简单变量调用
'''
    1、首先定义一些参数传递到前端的参数(下面的内容是在上面设置信息的基础上修改来的)
    在views中插入
        class Teacher():
        def teacher(self):
            return 'knowledge'
    
        def get_page(self):
            template=get_template('index.html')
            context={
                'name':'for',
                'age':23,
                'project':['python','linux','html'],
                'company': {"name": "xuegod", "position": "beijing"},
                'method': Teacher()
            }
        
            return HttpResponse(template.render(context))
    
    2、在index.html文件中插入
        <p>变量示例</p>
        {{ name }}<br>
        {{ age }}<br>
        {{ project }}<br>
        {{ company }}<br>
        注意下面这种调用方式
        {{ method.teacher }}<br>

    3、刷新页面就会展示出
        变量示例
        for
        23
        ['python', 'linux', 'html']
        {'name': 'xuegod', 'position': 'beijing'}
        knowledge 
'''

# 对于简单的变量，可以通过.来调用变量的索引和不需要传参的方法，比如name传递的是个字符串，那么就可以在前端利用模板语句进行这样的操作
'''
    1、在index.html中插入
        <p>变量示例</p>
        <p>变量直接调用： {{ name }}</p>
        <p>变量调用索引： {{ name.1 }}</p>
        <p>变量调用0参数的函数：{{ name.upper }}</p>
    2、刷新页面就会出现
        变量示例
        变量直接调用： for 
        变量调用索引： o  
        变量调用0参数的函数：FOR
'''

# 如果变量是列表，通过 . 索引可以调用指定的元素
'''
    1、在index.html中插入
        <p>变量示例</p>
        <p>变量是列表，调用列表: {{ project }}</p>
        <p>变量是列表，通过索引调用列表元素: {{ project.2 }}</p>
    2、刷新页面就会出现
        变量示例
        变量是列表，调用列表: ['python', 'linux', 'html']
        变量是列表，通过索引调用列表元素: html
'''

# 如果变量是字典，通过 . 键可以取到指定的值
'''
    1、在index.html中插入
        <p>变量示例</p>
        <p>变量是字典，调用字典: {{ company }}</p>
        <p>变量是字典，通过键调用字典值: {{ company.name }}</p>
    2、页面就会出现
        变量示例
        变量是字典，调用字典: {'name': 'xuegod', 'position': 'beijing'}
        变量是字典，通过键调用字典值: xuegod
'''

##### {%  %} 以大括号和%号包围的    标签语句
'''
    下面演示几种常见的语句，在高级部分还会学到自定义语句很更多语句使用的方法
    if语句，和python的if逻辑是完全一样，如果逻辑为真执行if，否则执行else，当然也支持elif语句，并且在HTML语句当中需要用
        {% endif %}来结束判断，因为在HTML当中python强调的缩进结束并没有什么卵用。
'''
# 简单的if判断
'''
    1、在index.html文件中插入
        <p>if 判断</p>
        {% if name == "mhile" %}
            <p> name is {{ name }}</p>
        {% elif name == "for" %}
            <p style = "color: red;"> name is {{ name }}</p>
        {% endif %}
    2、刷新页面后出现
        if 判断
        name is for
'''

# 在模板的判断语句当中也有一个简单的写法用来判断变量是否相等 ：{% ifequal %}，如果相等执行！
'''
    1、在index.html文件中插入
        # 与上面的if name=='for'是一样的，就是写法不同
        <p>ifequal 判断</p>
        {% ifequal name "mhile" %}
            <p> name is {{ name }}</p>
        {% else %}
            <p style = "color: red;"> name is {{ name }}</p>
        {% endifequal %}
    2、刷新页面后出现
        ifequal 判断
        name is for
'''

# for标签语句，for循环,如果后端传递到前端的是一个可迭代的序列，那么就可以通过循环的方式展示可迭代对象的每一个元素
'''
    1、在views.py中插入以下的内容
        from django.http import HttpResponse
        from django.template.loader import get_template
        News = [
            {"title": "for's editor","author": "for","time": "2018-06-13"},
            {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
            {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
            {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
            {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
            {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
        ]
        
        def  news(request):
            context = {"news":News}
            template = get_template("news.html")
            result = template.render(context)
            return HttpResponse(result)
    2、在urls.py中插入以下内容
        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import url
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('get_page/',views.get_page),
            url(r'^news', views.news),
    3、在news.html文件中插入
         <ul>
            {% for new in news %}
                <li style = "list-style: none;">
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
    4、刷新页面后就会出现
        for's editor     for     2018-06-13
        MK's editor     MK     2018-06-13
        CD's editor     CD     2018-06-13
        RM's editor     RM     2018-06-13
        Django's editor     Django     2018-06-13
        Twisted's editor     Twisted     2018-06-13
    
    总结上面的内容：
    {% for new in news %}

    {% endfor %}
    在这个标签当中，自动声明了一个变量叫做new作为循环赋值的变量，并且只在标签内部起作用，结合python for循环的例子，
    解释这段代码就是：
        声明一个变量叫做new，然后后对news进行迭代，把每次迭代出来的值赋值给new变量，并且形成一次循环。
'''

# 使用嵌套的for循环标签
'''
    1、在views.py中写入一下内容
        News = [
            {"title": "For's editor","author": "for","time": "2018-06-13"},
            {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
            {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
            {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
            {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
            {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
        ]
        
        def  news(request):
            context = {"news":News,"inner":[1,2,3]}
            template = get_template("news.html")
            result = template.render(context)
            return HttpResponse(result)
    2、在news.html中插入
        <ul>
            {% for num in inner %}
                <h1 style = "color: red;"> {{ num }} </h1>
                {% for new in news %}
                    <li style = "list-style: none;">
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
    3、刷新页面就会出现
        1
        For's editor     for     2018-06-13
        MK's editor     MK     2018-06-13
        CD's editor     CD     2018-06-13
        RM's editor     RM     2018-06-13
        Django's editor     Django     2018-06-13
        Twisted's editor     Twisted     2018-06-13
        2
        For's editor     for     2018-06-13
        MK's editor     MK     2018-06-13
        CD's editor     CD     2018-06-13
        RM's editor     RM     2018-06-13
        Django's editor     Django     2018-06-13
        Twisted's editor     Twisted     2018-06-13
        3
        For's editor     for     2018-06-13
        MK's editor     MK     2018-06-13
        CD's editor     CD     2018-06-13
        RM's editor     RM     2018-06-13
        Django's editor     Django     2018-06-13
        Twisted's editor     Twisted     2018-06-13
'''

# forloop,它在循环和嵌套循环过程当中起到了指针作用，可以很轻松的看到循环到了哪里，尤其是嵌套循环，forloop给开发者提供了类型python脚本的枚举（enumerate）的功能
'''
    1、在views.py文件中插入：
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
        
        def navigation(request):
            template = get_template("navigation.html")
            context = {"data":Navigation}
            result = template.render(context)
            return HttpResponse(result)
    2、在urls.py文件中插入
        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import url
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('get_page/',views.get_page),
            path('news/',views.news),
            path('navigation/',views.navigation)
            # url(r'^news', views.news),
]
    3、在navigation.html文件中插入
        {% for d in data %}
        <p> {{ d.label }} </p>
        <p> {{ forloop }} </p>
        {% endfor %}
    4、刷新页面就会显示
        python
        {'parentloop': {}, 'counter0': 0, 'counter': 1, 'revcounter': 9, 'revcounter0': 8, 'first': True, 'last': False}
        java
        {'parentloop': {}, 'counter0': 1, 'counter': 2, 'revcounter': 8, 'revcounter0': 7, 'first': False, 'last': False}
        php
        {'parentloop': {}, 'counter0': 2, 'counter': 3, 'revcounter': 7, 'revcounter0': 6, 'first': False, 'last': False}
        .net
        {'parentloop': {}, 'counter0': 3, 'counter': 4, 'revcounter': 6, 'revcounter0': 5, 'first': False, 'last': False}
        django
        {'parentloop': {}, 'counter0': 4, 'counter': 5, 'revcounter': 5, 'revcounter0': 4, 'first': False, 'last': False}
        flask
        {'parentloop': {}, 'counter0': 5, 'counter': 6, 'revcounter': 4, 'revcounter0': 3, 'first': False, 'last': False}
        spring
        {'parentloop': {}, 'counter0': 6, 'counter': 7, 'revcounter': 3, 'revcounter0': 2, 'first': False, 'last': False}
        xadmin
        {'parentloop': {}, 'counter0': 7, 'counter': 8, 'revcounter': 2, 'revcounter0': 1, 'first': False, 'last': False}
        django_ckeditor
        {'parentloop': {}, 'counter0': 8, 'counter': 9, 'revcounter': 1, 'revcounter0': 0, 'first': False, 'last': True}

    总结：
        上面的例子当中，调用了每次循环的forloop,可以看到这里通过
        Revcounter0:  倒序索引 （到0截止）
        Revcounter:  倒序 （到1截止）
        Parentloop： 父元素的forloop
        Counter: 计数（从1开始）
        Last: 是不是最后一个
        Counter0: 索引计数（从0开始）
        First: 是不是第一个
'''

# Forloop 提供了这样的参数可以轻松的掌握到每一个循环，接着看一下嵌套循环的内容
'''
    1、在views.py中插入
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
        
        def navigation(request):
            template = get_template("navigation.html")
            context = {"data":Navigation,"inner":[1,2,3]}
            result = template.render(context)
            return HttpResponse(result)
    2、在urls.py文件中插入
        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import url
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('get_page/',views.get_page),
            path('news/',views.news),
            path('navigation/',views.navigation)
            # url(r'^news', views.news),
        ]
    3、在navigation.html文件中插入
        {% for d in data %}
        <p> {{ d.label }} </p>
        <p> {{ forloop }} </p>
        {% endfor %}
    总结：
    这个例子侧重的看parentloop部分，这个部分来指出自己的父元素是谁。
    到这里，django 模板系统的for循环就学完了，接下来学习django 模板系统的 过滤器
    过滤器是django给开发者在前端修改已经调用的数据进行小调整的magic,过滤器django给开发者定义了好多，当然也可以自定义
'''

# 过滤器调用的方法
'''
    1、在views.py文件中插入
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
        
        def navigation(request):
            template = get_template("navigation.html")
            context = {"data":Navigation,"inner":[1,2,3]}
            result = template.render(context)
            return HttpResponse(result)
        2、在urls.py文件中插入
        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import url
        from App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('get_page/',views.get_page),
            path('news/',views.news),
            path('navigation/',views.navigation)
            # url(r'^news', views.news),
        ]
    3、过滤器调用方法
     {% for d in data %}
        <p> {{ d.label|upper }} </p>
    {% endfor %}
    4、刷新页面就会展示
    PYTHON
    JAVA
    PHP   
    .NET    
    DJANGO    
    FLASK    
    SPRING    
    XADMIN    
    DJANGO_CKEDITOR
'''

#####django官方常用的过滤器列表
'''
    过滤器	                    描述
    upper	                    以大写方式输出
    add	                        给value加上一个数值
    addslashes	                单引号加上转义号
    capfirst	                第一个字母大写
    center	                    输出指定长度的字符串，把变量居中
    Cut	                        删除指定字符串
    date	                    格式化日期
    default	                    如果值不存在，则使用默认值代替
    default_if_none	            如果值为None, 则使用默认值代替
    dictsort	                按某字段排序，变量必须是一个dictionary
    dictsortreversed	        按某字段倒序排序，变量必须是dictionary
    divisibleby	                判断是否可以被数字整除
    escape	                    按HTML转义，比如将”<”转换为”&lt”
    filesizeformat	            增加数字的可读性，转换结果为13KB,89MB,3Bytes等
    first	                    返回列表的第1个元素，变量必须是一个列表
    floatformat	                转换为指定精度的小数，默认保留1位小数
    get_digit	                从个位数开始截取指定位置的数字
    join	                    用指定分隔符连接列表
    length	                    返回列表中元素的个数或字符串长度
    length_is	                检查列表，字符串长度是否符合指定的值
    linebreaks	                用<p>或<br>标签包裹变量
    linebreaksbr	            用<br/>标签代替换行符
    linenumbers	                为变量中的每一行加上行号
    ljust	                    输出指定长度的字符串，变量左对齐
    lower	                    字符串变小写
    make_list	                将字符串转换为列表
    pluralize	                根据数字确定是否输出英文复数符号
    random	                    返回列表的随机一项
    removetags	                删除字符串中指定的HTML标记
    rjust	                    输出指定长度的字符串，变量右对齐
    slice	                    切片操作， 返回列表
    slugify	                    在字符串中留下减号和下划线，其它符号删除，空格用减号替换
    stringformat	            字符串格式化，语法同python
    time	                    返回日期的时间部分
    timesince	                以“到现在为止过了多长时间”显示时间变量
    timeuntil	                以“从现在开始到时间变量”还有多长时间显示时间变量
    title	                    每个单词首字母大写
    truncatewords	            将字符串转换为省略表达方式
    truncatewords_html	        同上，但保留其中的HTML标签
    urlencode	                将字符串中的特殊字符转换为url兼容表达方式
    urlize	                    将变量字符串中的url由纯文本变为链接
    wordcount	                返回变量字符串中的单词数
    yesno	                    将布尔变量转换为字符串yes, no 或maybe
'''













