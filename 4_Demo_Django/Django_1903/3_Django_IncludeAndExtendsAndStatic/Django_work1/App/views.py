from django.shortcuts import render
from App import models
# 首页
def func_index(request):
    return render(request,'index.html')
# register页
def func_register(request):
    # 注意这个位置request.method=='POST',一定要写method
    if request.method=='POST':
        Title=request.POST.get('title')
        First_Name=request.POST.get('first_name')
        Last_Name=request.POST.get('last_name')
        Email=request.POST.get('email')
        Mobile=request.POST.get('mobile')
        Address=request.POST.get('address')
        District=request.POST.get('district')
        City=request.POST.get('city')
        Zipcode=request.POST.get('zipcode')
        # 在服务器中输出提交的内容，也可以不写
        print(Title,First_Name,Last_Name,Email,Mobile,Address,District,City,Zipcode)
        # 把数据保存到数据库
        models.Register.objects.create(
            # Models.py中的变量名=views.py中的变量名
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
# signup页

def func_signup(request):
    # 注意这个位置request.method=='POST',一定要写method
    if request.method=='POST':
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        Password2=request.POST.get('password2')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        # 在服务器中输出提交的内容，也可以不写
        print(Username,Password,Password2,Email,Phone)
        # 保存到数据库
        models.Signup.objects.create(
            # Models.py中的变量名=views.py中的变量名
            username=Username,
            password=Password,
            password2=Password2,
            email=Email,
            phone=Phone,
        )

    return render(request,'signup.html')

def func_login(request):
    # 注意这个位置request.method=='POST',一定要写method
    if request.method=='POST':
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        # 在服务器中输出提交的内容，也可以不写
        print(Username,Password)
        # 保存到数据库
        models.Login.objects.create(
            # Models.py中的变量名=views.py中的变量名
            username=Username,
            password=Password
        )
    return render(request,'login.html')
# survey
def func_survey(request):
    # 注意，这个地方一定要是request.method=='POST'
    if request.method=='POST':
        Group1 = request.POST.get('group1')
        Description = request.POST.get('description')
        Choice1 =request.POST.get('choice1')
        Choice2 =request.POST.get('choice2')
        Choice3 =request.POST.get('choice3')
        Occupation =request.POST.get('occupation')
        Income =request.POST.get('income')
        Age =request.POST.get('age')
        Name =request.POST.get('name')
        Email =request.POST.get('email')
        Gender =request.POST.get('gender')
        Message =request.POST.get('message')
        # 在服务器中输出，也可以不写
        print(Group1,Description,Choice1,Choice2,Choice3,Occupation,Income,Age,Name,Email,Gender,Message)
        # 保存到数据库
        models.Survey.objects.create(
            # models.py中的变量名也就是表的字段名=views.py中的变量名
            group1=Group1,
            description=Description,
            choice1=Choice1,
            choice2=Choice2,
            choice3=Choice3,
            occupation=Occupation,
            income=Income,
            age=Age,
            name=Name,
            email=Email,
            gender=Gender,
            message=Message
        )
    return render(request,'survey.html')
# Applications
def func_application(request):
    if request.method=='POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Address1 = request.POST.get('address1')
        Address2 = request.POST.get('address2')
        City = request.POST.get('city')
        Zipcode = request.POST.get('zipcode')
        Gender = request.POST.get('gender')
        Expectedsalary = request.POST.get('expectedsalary')
        Browse = request.POST.get('browse')
        Message = request.POST.get('message')
        # 在服务器输出，也可以不写
        print(Name,Email,Address1,Address2,City,Zipcode,Gender,Expectedsalary,Browse,Message)
        # 保存在数据库中
        models.Applicaltions.objects.create(
            # models.py中的变量名也就是字段名=views.py中的变量名
            name=Name,
            email=Email,
            address1=Address1,
            address2=Address2,
            city=City,
            zipcode=Zipcode,
            gender=Gender,
            expectedsalary=Expectedsalary,
            browse=Browse,
            message=Message
        )
    return render(request,'application.html')