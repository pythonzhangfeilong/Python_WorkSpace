from django.shortcuts import render
from ajax_App import models
def func_ajax(request):
   if request.method=='GET':
      username=request.GET.get('username')
      password=request.GET.get('password')
      emaile=request.GET.get('email')
      phone=request.GET.get('phone')
      print(username,password,emaile,phone)

      models.Ajax.objects.create(
         Username=username,
         Password=password,
         Email=emaile,
         Phone=phone
      )
   return render(request,'ajax.html')
