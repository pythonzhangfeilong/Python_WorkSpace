from django.shortcuts import render
from ajax_App import models
def func_ajax(request):
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      emaile=request.POST.get('email')
      phone=request.POST.get('phone')
      print(username,password,emaile,phone)

      models.Ajax.objects.create(
         Username=username,
         Password=password,
         Email=emaile,
         Phone=phone
      )
   return render(request,'ajax.html')
