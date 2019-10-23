from django.db import models
class UserData(models.Model):
    First_Name=models.CharField(max_length=32,verbose_name='名')
    Last_Name=models.CharField(max_length=32,verbose_name='姓',blank=True)
    Email=models.CharField(max_length=32,verbose_name='邮箱',blank=True)
    Password=models.CharField(max_length=32,verbose_name='密码',blank=True)
    Confirm_Password=models.CharField(max_length=32,verbose_name='确认密码',blank=True)
    
    # 不管是谁调用都返回下面制定的函数
    def __str__(self):
        return self.First_Name
