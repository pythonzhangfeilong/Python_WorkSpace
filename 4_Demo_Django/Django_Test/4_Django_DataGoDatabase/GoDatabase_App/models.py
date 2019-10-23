from django.db import models

# 创建的这个类名就是表名，必须继承models.Model
class UserData(models.Model):
    # 变量名username是表中的字段名
    username=models.CharField(max_length=32,verbose_name='用户名')
    # 变量名password是表中的字段名
    password=models.CharField(max_length=32,verbose_name='密码')

    # 凡是打印类的实例，都会显示出返回这个参数
    def __str__(self):
        return '用户名：%s'%self.username