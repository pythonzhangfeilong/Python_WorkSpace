from django.shortcuts import render
# forms中的UserForm类导过来
from Form_class_App.forms import UserForm
def func_form(request):
    # 将类实力为对象
    obj=UserForm()
    return render(request,'form.html',context={'obj':obj})