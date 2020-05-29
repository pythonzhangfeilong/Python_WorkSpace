from django.db import models
# register页
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

# signup
class Signup(models.Model):
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')
    password2=models.CharField(max_length=32,verbose_name='确认密码')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    phone=models.CharField(max_length=11,verbose_name='手机号')

    def __str__(self):
        return self.username

# login
class Login(models.Model):
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')
    def __str__(self):
        return self.username

# survey
class Survey(models.Model):
    group1=models.CharField(max_length=32,verbose_name='选择项')
    description=models.CharField(max_length=128,verbose_name='输入段')
    choice1=models.CharField(max_length=32,verbose_name='选择一',null=True)
    choice2=models.CharField(max_length=32,verbose_name='选择二',null=True)
    choice3=models.CharField(max_length=32,verbose_name='选择三',null=True)
    occupation=models.CharField(max_length=32,verbose_name='职业')
    income=models.CharField(max_length=32,verbose_name='收入水平')
    age=models.CharField(max_length=32,verbose_name='年龄')
    name=models.CharField(max_length=32,verbose_name='名字')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    gender=models.CharField(max_length=32,verbose_name='性别')
    message=models.CharField(max_length=128,verbose_name='消息')

    def __str__(self):
        return self.group1
# Applications
class Applicaltions(models.Model):
    name=models.CharField(max_length=32,verbose_name='全名')
    email=models.CharField(max_length=32,verbose_name='邮箱')
    address1=models.CharField(max_length=32,verbose_name='地址1',null=True)
    address2=models.CharField(max_length=32,verbose_name='地址2',null=True)
    city=models.CharField(max_length=32,verbose_name='城市')
    zipcode=models.CharField(max_length=32,verbose_name='邮编')
    gender=models.CharField(max_length=32,verbose_name='性别')
    expectedsalary=models.CharField(max_length=32,verbose_name='预计薪酬')
    browse=models.CharField(max_length=32,verbose_name='上传文件',null=True)
    message=models.CharField(max_length=128,verbose_name='建议')

    def __str__(self):
        return self.name