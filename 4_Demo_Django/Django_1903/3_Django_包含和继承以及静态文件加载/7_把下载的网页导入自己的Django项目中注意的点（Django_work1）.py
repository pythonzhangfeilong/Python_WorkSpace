# 把下载的网页导入自己的Django项目中
'''
    1、首先就是settings.py中最后添加：
        注意：单词不要写错，以列表的形式包裹
        STATICFILES_DIRS=[
            os.path.join(BASE_DIR,'static')
        ]
    2、每一个响应的页面都是在views.py中有一个函数在执行
        def func_index(request):
            return render(request,'index.html')
    3、在urls.py中配置响应的页面地址
        首先配置的页面地址的首页
            path('index/',views.func_index),
        然后是在首页点击项的地址
            path('index/register/',views.func_register),
            path('index/signup/',views.func_signup),
            path('index/login/',views.func_login),
            path('index/survey/',views.func_survey),
            path('index/application/',views.func_application)
    4、接下来就是首页html中a标签里的href地址
        <a href="/index/register/" class="tm-white-text" >01. Register</a>
'''




















