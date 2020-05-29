from django.db import models

class Tijiao(models.Model):
    file=models.FileField(verbose_name='文件')

    def __str__(self):
        return '文件：%s'%self.file

