from django.db import models

class Example(models.Model):
    name=models.CharField(max_length=32,verbose_name='名字')
    type=models.CharField(max_length=32,verbose_name='类型')
