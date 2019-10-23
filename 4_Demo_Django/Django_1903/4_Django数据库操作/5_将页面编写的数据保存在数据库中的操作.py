'''
1、首先要查看页面有几个字段，将他们分别写在models.py文件中
class Register(models.Model):
    title=models.CharField(max_length=32,verbose_name='先生还是女士')
    first_name=models.CharField(max_length=32,verbose_name='姓')
    last_name=models.CharField(max_length=32,verbose_name='名')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    mobile=models.CharField(max_length=11,verbose_name='手机号码')
    address=models.CharField(max_length=32,verbose_name='居住地址')
    district=models.CharField(max_length=32,verbose_name='区')
    city=models.CharField(max_length=32,verbose_name='城市')
    zipcode=models.CharField(max_length=32,verbose_name='邮政编码')
    def __str__(self):
        return self.last_name
'''

'''
2、在views.py中写入：
# register页
def func_register(request):
    # 注意，这个位置request.method=='POST',一定要写method
    if request.method=='POST':
    # 注意小括号里的参数是models.py中的变量名也就是表的字段名
        Title=request.POST.get('title')
        First_Name=request.POST.get('first_name')
        Last_Name=request.POST.get('last_name')
        Email=request.POST.get('email')
        Mobile=request.POST.get('mobile')
        Address=request.POST.get('address')
        District=request.POST.get('district')
        City=request.POST.get('city')
        Zipcode=request.POST.get('zipcode')
        # 注意，在服务器中输出提交的内容，也可以不写
        print(Title,First_Name,Last_Name,Email,Mobile,Address,District,City,Zipcode)
        # 把数据保存到数据库
        models.Register.objects.create(
            # 注意，Models.py中的变量名=views.py中的变量名
            title=Title,
            first_name=First_Name,
            last_name=Last_Name,
            email=Email,
            address=Address,
            district=District,
            city=City,
            zipcode=Zipcode,
        )
    return render(request,'register.html')
'''

######################编写页面的时候注意的点######################
'''
1、首先数据库的配置和设置，把settings.py中MIDDLEWARE里面的'django.middleware.csrf.CsrfViewMiddleware',跨域请求注释掉
2、先确认html文件中form表单的actions属性写的是提交访问的页面,
3、在models.py文件中，创建的类名就是表名，且首字母一定要大些，继承固定的models.Model,变量名就是字段的名称
4、models.py中写好之后，在pycharm的Terminal中执行python manage.py makemigrations同步数据库，再执行python manage.py migrate生成数据库表
5、接下来就是models.py文件中编写时一定要注意：
    ①# 注意，这个位置request.method=='POST',一定要写method
    if request.method=='POST':
    
    ②if request.method=='POST':
    # 注意小括号里的参数是models.py中的变量名也就是表的字段名
        Title=request.POST.get('title')
        First_Name=request.POST.get('first_name')
    
    ③# 把数据保存到数据库
        models.Register.objects.create(
            # 注意，Models.py中的变量名=views.py中的变量名
            title=Title,
            first_name=First_Name,
    ④如果python manage.py migrate建表时出现No migrations to apply.
    在数据库中使用delete from django_migrations where id='删除的id';处理一下
    
    ⑤如果出现1048, "Column 'browse' cannot be null"找到browse哪一行和那个字段，在创建数据库的时候给一个null=True
'''


















