# ajax提交文件对象__保存到项目制定文件夹中
'''
1、在settings.py文件中找到DATABASE，写入：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'database_ajax_tijiaos',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSSWORD': ''
    }
}

2、在settings.py文件中找到MIDDLEWARE，将里面的'django.middleware.csrf.CsrfViewMiddleware'注释掉

3、在settings.py文件中找到LANGUAGE_CODE和TIME_ZONE修改为
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

4、在templates文件夹中创建一个ajax_tijiao.html,写入：
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ajax</title>
</head>
<body>
{#enctype="multipart/form-data" //不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。#}
<form action="/ajax_tijiao/" method="post" enctype="multipart/form-data">
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

5、在views.py中写入：
from django.shortcuts import render
from django.http import JsonResponse
import os
def func_ajax_tijiao(request):
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
    return render(request,'ajax_tijiao.html')

6、在项目的最外层文件夹下创建media文件夹，在media文件夹下创建images文件夹

7、启动Django服务，在浏览器访问http://127.0.0.1:8000/ajax_tijiao/，就可以提交图片到指定文件夹
'''


























