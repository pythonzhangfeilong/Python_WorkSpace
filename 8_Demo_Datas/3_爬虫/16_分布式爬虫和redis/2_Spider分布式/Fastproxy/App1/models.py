from django.db import models

# Create your models here.

class Proxy(models.Model):
    objects = models
    ip=models.CharField(max_length=20)
    port=models.CharField(max_length=20)
    Anonymity = models.CharField(max_length=20)
    # 类型
    type = models.CharField(max_length=20)
    # 位置
    position = models.CharField(max_length=50)
    # 响应时间
    response_time = models.CharField(max_length=20)
    # 最后验证时间
    Last_validation_time =models.CharField(max_length=20)