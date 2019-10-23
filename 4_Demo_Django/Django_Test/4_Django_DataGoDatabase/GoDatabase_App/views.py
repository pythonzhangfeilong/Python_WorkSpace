from django.shortcuts import render
# 导入models文件
from GoDatabase_App import models
def func_index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库,userData折models中的类名，也就是标名因为models中变量名设置的是username和password所以就出现了下面的情况
        models.UserData.objects.create(username=username,password=password)
    # 从数据库中读取所有的数据
    # user_Data_list=models.UserData.objects.all()
    return render(request, 'index.html')
