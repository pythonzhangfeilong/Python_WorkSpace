from django.shortcuts import render
from APPS import models
# Create your views here.
def func(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存在数据库中
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取所有的数据
    user_list = models.UserInfo.objects.all()
    return render(request, 'func.html', {'date': user_list})