from django.db import models
class Author(models.Model):
    gender_choice = (
        ("M","Male"),
        ("F","Female"),
    )
    name = models.CharField(max_length = 32,verbose_name = "作者姓名")
    age = models.IntegerField(verbose_name = "作者年龄",blank = True,null = True)
    gender = models.CharField(max_length = 2,choices = gender_choice,verbose_name = "作者性别",blank = True,null = True)
    email = models.EmailField(verbose_name = "作者邮箱",blank = True,null = True)
    phone = models.CharField(max_length = 11,verbose_name = "作者电话",blank = True,null = True)

    def __str__(self):
        return "作者:%s"%self.name

class Classify(models.Model):
    label = models.CharField(max_length = 32,verbose_name = "分类标签")
    description = models.TextField(verbose_name = "分类描述")

    def __str__(self):
        return "标签:%s" % self.label


class Article(models.Model):
    title = models.CharField(max_length = 32,verbose_name = "文章标题")
    time = models.DateField(verbose_name = "文章发表日期")
    description = models.TextField(verbose_name = "文章描述")
    content = models.TextField(verbose_name = "文章内容")

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    classify = models.ManyToManyField(Classify)

    def __str__(self):
        return "文章:%s" % self.title



























