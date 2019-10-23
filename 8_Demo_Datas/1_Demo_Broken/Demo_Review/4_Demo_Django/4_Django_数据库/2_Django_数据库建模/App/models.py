from django.db import models

class Teacher(models.Model):
    school=models.CharField(max_length=32,verbose_name='学校名称')
    system=models.CharField(max_length=32,verbose_name='院系')
    major=models.CharField(max_length=32,verbose_name='专业')
    teacher_name=models.CharField(max_length=32,verbose_name='老师的名字')

    # 类当中设定了__str__之后，凡是要打印类的实例，都会返回指定的这个字符串
    def __str__(self):
        return self.school

    # 类当中设定了__repr__ 会更加的彻底，实例之间返回名称
    def __repr__(self):
        return 'Hello'