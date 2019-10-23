'''
1、首先在views.py文件中写入：
from django.shortcuts import render

user_Data_list=[]       # 创建一个空列表
def func_index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print('用户名:'+username,'密码:'+password)
        temp={'user':username,'pwd':password}       # 发送过来的用户名和密码构建一个字典
        user_Data_list.append(temp)             # 将构建的字典传递到创建的列表中
    return render(request,'index.html',{'data':user_Data_list})     # {'data':user_Data_list}将用户列表供render渲染index
'''

'''
2、在templates文件夹中创建index.html文件，写入
<body>
    <h1>用户输入</h1>
    <form action="/index/" method="post">
        {% csrf_token %}
        用户名:<input type="text" name="username"/>
        <br>
        密码:<input type="password" name="password"/>
        <br>
        <button type="submit">提交</button>
    </form>

    <div style="border: red 1px solid">
        <h1>用户展示</h1>
        <thead>
            <tr>用户名</tr>
            <tr>密码</tr>
        </thead>
        <br>
        <tbody>
            {% for item_data in data %}
                <tr>
                    <td>{{ item_data.user }}</td>
                    <td>{{ item_data.pwd }}</td>
                    <br>
                </tr>
            {% endfor %}
        </tbody>
    </div>
</body>
'''

'''
3、在urls.py文件中写入：
    from Dongtai_App import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/',views.func_index)
    ]
'''

'''
4、启动Django服务，在浏览器地址中输入http://127.0.0.1:8000/index/
在页面提交的内容不止会在服务中显示，也会展示在页面中
'''


