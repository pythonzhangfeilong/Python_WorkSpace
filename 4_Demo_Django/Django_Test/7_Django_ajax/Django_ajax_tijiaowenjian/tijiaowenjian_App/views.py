from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
#####下面的是利用from表单把图片保存到数据库中
# from tijiaowenjian_App import models
# def func_ajax(request):
#     if request.method=='POST':
#         file=request.POST.get('file')
#
#         models.Tijiao.objects.create(
#             file=file
#         )
#     return render(request,'ajax.html')

####下面的是利用ajax把图片保存到项目制定文件夹中

import os
def filetest(request):
    if request.method=='POST' and request.POST:
        #获取文件名字
        filename = request.FILES.get('file').name
        #拼接文件路径，课存储到model中方便项目寻找到
        print(filename)
        filepath = os.path.join('media/images',filename)
        #保存图片
        with open(filepath,'wb') as f:
            # UploadedFile.chunks()：如果上传的文件足够大需要分块就返回真。默认的这个值是2.5M，当然这个值是可以调节的。
            for chunk in request.FILES.get('file').chunks():
                if chunk:
                    f.write(chunk)

        return JsonResponse({'status':'success'})
    return render(request,'ajax.html')





