from django.db import models

class Ajax(models.Model):
    Username=models.CharField(max_length=32,verbose_name='用户名')
    Password=models.CharField(max_length=32,verbose_name='密码')
    Email=models.EmailField(max_length=32,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='手机号')


    def __str__(self):
        return '用户名%s'%self.Username

