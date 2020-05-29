'''
    在很多的网站中尤其是电商和企业网站，往往整个网站有N多的页面，但是样式是大同小异的，比如导航栏、侧边栏、页面尾部，
        这样的看来网页的代码是有一些冗余的，为了避免重复的造轮子，Django推出了俩个标签include包含和extends继承
'''
#####include包含：指的是将一个页面中过的内容添加到另一个页面中
# 1、首先在views.py文件中,写入:
'''
    #####render和render_to_response的区别
        render是需要request参数的
        render_to_response不需要request参数
    
    from django.shortcuts import render
    from django.shortcuts import render_to_response
    def func_yuanwork(request):
        return render(request,'yuanwork.html')
'''
# 2、创建yuanwork.html写入：
'''
    <div>{% include 'include_work.html' %}</div>
'''

# 3、在urls.py中写入:
'''
    from include_App import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('yuanwork/',views.func_yuanwork)
    ]
'''

# 4、创建include_work.html中写入被包含的内容：
'''
    <div style="background: red">包含</div>
'''

# 5、启动Django项目，访问地址：http://127.0.0.1:8000/yuanwork/
'''
    这样访问yuanwork的HTML就会将invlude_work.html中的内容包含显示出来
'''













