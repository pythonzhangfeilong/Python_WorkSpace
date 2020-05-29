from django.db import models

class Index(models.Model):
    Username = models.CharField(max_length=12,verbose_name='用户名',null=True)
    Password = models.CharField(max_length=12,verbose_name='密码')
    Email = models.EmailField(max_length=12,verbose_name='邮箱')
    Phone = models.CharField(max_length=12,verbose_name='手机号')

    class Meta():
        verbose_name='用户名'
        verbose_name_plural=verbose_name