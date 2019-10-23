#####  |  用于变量后进行修饰的过滤器
'''
    过滤器是django给开发者在前端修改已经调用的数据进行小调整的magic,过滤器django给开发者定义了好多，当然也可以自定义
'''
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
        def navigation(request):
            context={'navigation':Navigation}
            return render(request,'modification.html',context=context)
    2、在templates的文件夹中在modification.html的文件中写入下面的数据
        {# | 过滤修饰#}
        {% for data in navigation %}
            <p>{{ data.label | upper }}</p>
        {% endfor %}
    3、在项目文件夹中找到urls.py文件写入下面的数据
        from App import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                # https://127.0.0.1:8000/index,路径拼接使用的是path后面的第一个参数，第二个参数views.get_page实际是调用的函数
                # path('index/',views.index)                  # 模板系统加载的url
                # path('index/',views.get_page)               # 给前端传递参数的url
                # path('for/',views.news)                     # 给前端传递参数的url
                # path('forloop/',views.forloop)              # 给前端传递参数的url
                path('modification/',views.navigation)      # 给前端传递url
            ]
'''
















