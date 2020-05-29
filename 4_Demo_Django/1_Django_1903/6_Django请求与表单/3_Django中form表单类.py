#####Django中的form表单类
'''
    除了html中有form表单，在Django中也有一个form表单类，用来定义form表单

    form表单的作用:提供了完善的前后端封装，免去了js校验、数据整合、报错等的编写，让变成更加快捷
'''

#1、form表单的定义：
'''
    1、form表单的定义通过Django下面的form类进行，过程和Django模型定义相似，在App文件夹中创建一个forms.py的文件，写入：
        from django import forms
        class UserForm(forms.Form):
            username = forms.CharField(label='联系人姓名')
            password = forms.CharField(min_length=6, label='联系人密码')
            email = forms.CharField(max_length=32, label='联系人邮箱')
            phone = forms.CharField(min_length=11, label='联系人电话')
    2、在views.py中写入：
        # forms中的UserForm类导过来
        from Form_class_App.forms import UserForm
        def func_form(request):
            # 将类实力为对象
            obj=UserForm()
            return render(request,'form.html',context={'obj':obj})
    3、在templates的文件夹中创建一个form.html并且写入：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>form</title>
        </head>
        <body>
        {#.as_就是谁要用什么标签修饰#}
            {#as_p的意思就是obj用p标签来修饰#}
            {{ obj.as_p }}
        
            {#as_ul的意思就是obj用ul标签来修饰#}
            {{ obj.as_ul }}
        
        {#给传递的参数添加样式#}
        <p>
            <label style="color: red">{{ obj.username.label }}</label>
            {#添加过的内容用列表的形式展示#}
            {{ obj.username }}
        </p>
        
        <p>
            <label style="color: red">{{ obj.password.label }}</label>
            {#添加过的内容用列表的形式展示#}
            {{ obj.password }}
        </p>
        
        <p>
            <label style="color: red">{{ obj.email.label }}</label>
            {#添加过的内容用列表的形式展示#}
            {{ obj.email }}
        </p>
        
        <p>
            <label style="color: red">{{ obj.phone.label }}</label>
            {#添加过的内容用列表的形式展示#}
            {{ obj.phone }}
        </p>
        
        {#使用for循环实现上面的效果#}
        {% for i in obj %}
            <label style="color: red">{{ i.label }}</label>
            {#添加过的内容用列表的形式展示#}
            {{ i }}
        {% endfor %}
        </body>
        </html>
    4、在项目的根目录中配置urls.py,写入：
        from Form_class_App import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('form/',views.func_form)
        ]
'''

# 2、form字段里面常用的字段和对应的参数：
'''
常用字段：
    1、charfield  对应单行输入框
    2、booleanfield  对应checkbox选择框
    3、choicefield 对应下拉菜单选择框   重要参数choice
    4、datafield  对应一个单行输入框，但是会自动转化为日期类型
    5、emailfield  对应输入框，自动验证是否是邮件地址
    6、filefield  对应文件上传选项
    7、filepathfiled 对应一个（文件组成的下拉菜单）选择，必须参数path=''.选项为这个地址里边所有的文件。可选参数recursive=True是否包含子文件夹里的文件
    8、imagefield  图片上传按钮。需要pillow模块
    9、urlfield  对应输入框 自动验证是否为网址格式
字段常用的参数
    1、rqeuired    字段是否为必填 默认为True
    2、label  类似于输入框前边的提示信息
    3、initial 初始值（占位符）就是给出一个默认值
    4、help_text  字段的辅助描述
    5、error_message={}  覆盖｛｛form.name.error｝｝信息
    6、disable  字段是否可以修改 
    7、widget 负责渲染网页上HTML表单的输入元素和提取提交的原始数据。
    8、max_length 最大长度
    9、min_length 最小长度
'''
















