from django.db import models

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=32,verbose_name='教师名字')
