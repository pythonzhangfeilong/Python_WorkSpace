#####现在的网站,尤其是企业的网站和电商的网站,会发现一个页面会出现多个相同的页面,但是这些页面的样式大同小异
'''
    比如导航栏、侧边栏、页面的尾部

    这样的网站看起来是有一些冗余的，为了代码的一至性和避免重复的造轮子，Django推出了俩个标签：
        include包含
        extends继承
'''

#####包含include：指的是将一个网页加载到另一个网页当中
'''
    1、在App的文件夹中，找到views.py文件，写入：
        from django.shortcuts import render
        def framework_page(request):
            return render(request,'framework.html')
    2、在templates文件夹中创建一个include.html,写入：
        <div style="background-color: green">绿色</div>
    3、在项目的根目录中找到urls.py文件，写入：
        from includeANDextends import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('feamework/',views.framework_page)
        ]
    4、在templates文件夹中创建一个framework.html，写入：
        {% include 'include.html' %}
    5、完成上面的几步，就把include.html中的内容放在了framework.html中
    6、在浏览器中输入http://127.0.0.1:8000/framework/，就会显示出include.html中的内容
'''

#####entends继承：相比包含，继承要先设计好继承的页面，通常命名为base.html
'''
    base.html当中编写了其他网页的共性东西，比如抬头、结尾，而其中的内容需要其他页面的修改，个性的东西被
        block标签包围，便利的内容为默认内容
        
    1、首先在App文件中找到views.py文件，写入：
        from django.shortcuts import render
        def extends_base(request):
            return render(request,'extends_base.html')
    2、在templates的文件夹中，创建extends_base.html并且，写入：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>extends_base</title>
        </head>
        <body>
            {% extends 'base.html' %}
            {% block title %}
                extends base
            {% endblock %}
        
            {% block content %}
                hello word
            {% endblock %}
        </body>
        </html>
    3、在项目的根目录中找到urls.py文件，写入：
        from includeANDextends import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('extends/',views.extends_base)
        ]
    4、在templates的文件夹中，创建base.html并且，写入：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>
                {% block title %}
                    Title
                {% endblock %}
            </title>
        </head>
        <body style="background-color: #0f74a9;color:white">
            {% block content %}
            
            {% endblock %}
        </body>
        </html>
    总结：extend_base.html继承了base.html，并且根据自己的需求修改了title和content块儿，这两个块儿在
        base页当中定义，在extend_base.html也修改，其中title有默认值，加入在extend页面当中不进行修改，
        就采用默认值   
'''











































