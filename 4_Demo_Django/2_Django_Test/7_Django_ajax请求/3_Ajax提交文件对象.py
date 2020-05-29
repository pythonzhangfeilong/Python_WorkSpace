#####ajax提交文件对象
# 一、form表单提交文件对象__保存到数据库中
'''
1、在templates文件夹中创建一个ajax.html,写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
</head>
<body>
    <div style="border: solid 1px red">
        <input type="file" name="file"><br>
        <input type="submit" name="提交">
    </div>
</body>
</html>

2、在views.py中写入：
from django.shortcuts import render
def func_ajax(request):
    return render(request,'ajax.html')

3、在urls.py中写入：
from tijiaowenjian_App import views
urlpatterns = [
    path('tijiao/',views.func_ajax)
]

4、在models中写入：
class Tijiao(models.Model):
    file=models.FileField(verbose_name='文件')

    def __str__(self):
        return '文件：%s'%self.file
5、在pycharm的Terminal中写入python manage.py check检查有没有错误
   在pycharm的Terminal中写入python manage.py makemigrations生成数据库表
   在pycharm的Terminal中写入python manage.py migrate迁移数据库表
6、修改vviews.py中写入：
from django.shortcuts import render
from tijiaowenjian_App import models
def func_ajax(request):
    if request.method=='POST':
        file=request.POST.get('file')

        models.Tijiao.objects.create(
            file=file
        )
    return render(request,'ajax.html')
7、注销settings.py中的跨域请求验证
8、修改settings.py中的
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
9、启动Django服务，访问http://127.0.0.1:8000/tijiao/
'''

# 二、ajax提交文件对象__保存到项目制定文件夹中
'''
1、在templates文件夹中创建一个ajax.html,写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
</head>
<body>
{#enctype="multipart/form-data" //不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。#}
<form action="/tijiao/" method="post" enctype="multipart/form-data">
        <input type="file" name="file"><br>
        <input type="submit" id="btn" name="提交">
</form>
<script>
    $(function () {
        $("#btn").click(function () {
            //创建一个FormData对象用来存储数据
            var file_obj = new FormData;
            //通过jquery的的属性操作找到上传的文件,
            // 注意files方法是js对象的特有的方法，所以需要将jquery对象索引转化成js对象调用此方法
            file_obj.append('file', $("input[type='file']")[0].files[0]);
            //jquery的属性操作获取csrftoken值来防御CSRF攻击
            file_obj.append('csrfmiddlewaretoken',     $('[name=csrfmiddlewaretoken]').val());
            $.ajax({
                url: '/reqform/filetest/',
                type: 'post',
                processData: false,//不让jQuery处理我的file_obj
                contentType: false,//不让jQuery设置请求的内容类型
                data: file_obj,
                //成功回调函数
                success: function (res) {
                    console.log(res)
                }
            })
        })
    })
</script>
</body>
</html>

2、在views.py中写入：
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
3、urls.py中写入：
from tijiaowenjian_App import views
urlpatterns = [
    path('tijiao/',views.filetest)
]
4、在项目的最外层文件创建media文件夹，再在里面创建images文件夹
'''

































