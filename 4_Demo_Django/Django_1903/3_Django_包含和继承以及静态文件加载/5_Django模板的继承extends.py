#####Django模板的继承
'''
    相对于包含的内容，继承时先要设计好被继承的页面通常被命名为base.html，base.html当中编写了其他网页共性的东西，
        比如说抬头，比如说结尾，而其中其他页面需要修改，个性的东西被block标签包围，标签里的内容为默认内容。
'''

# 1、在templates的文件夹中创建base.html,写入：
'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            {% block title %}
                base_title
            {% endblock %}
        </title>
    </head>
    <body style="background-color: red;color: white">
        {% block context %}
            
        {% endblock %}
    </body>
    </html>
'''

# 2、首先在views.py中编写:
'''
    from django.shortcuts import render
    def func_jicheng(request):
        return render(request,'yuan_work.html')
'''

# 3、在templates的文件夹中创建yuan_work.html，写入：
'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>yuan_work</title>
    </head>
    <body>
        {% extends 'base.html' %}
    
        {% block title %}
            yuan_work base_title
        {% endblock %}
    
        {% block context %}
            Hello Work
        {% endblock %}
    </body>
    </html>
'''

# 4、在urls.py文件中写入
'''
    from extends_App import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('extends_func/',views.func_jicheng)
    ]
'''

# 5、在浏览器地址栏拼接访问：http://127.0.0.1:8000/extends_func/
'''
    逻辑总结：
        也就是编写一个一会儿将要被继承的base.html文件，再写一个yuan_work.html文件去继承base.html中的公共方法
'''

