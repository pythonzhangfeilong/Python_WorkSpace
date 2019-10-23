from django.shortcuts import render
from work_App import models
def func(request):
    # 注意POST一定要大写
    if request.method=='POST':
        # get括号里面的字体内容要与HTML中标签里name一致
        First_Name = request.POST.get('First Name')
        Last_Name = request.POST.get('Last Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password =request.POST.get('Confirm Password')
        print(First_Name,Last_Name,Email,Password,Confirm_Password)
        models.UserData.objects.create(
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email=Email,
            Password=Password,
            Confirm_Password=Confirm_Password,
        )
    return render(request,'index.html')
