#####4、ORM数据库关系
'''
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

上面的内容完成之后就是：
    第一步：检测配置和模型编写是否有误：
        在pycharm的Terminal中输入python manage.py check，出现System check identified no issues (0 silenced).
        就是配置成功，如果出现报错的内容，在项目的根目录__init__.py文件中写入下面的内容，不报错就不要写：
            import pymysql
            pymysql.install_as_MySQLdb()
    第二步：进行数据集语句的生成和数据库操作记录的生成
        在pycharm的Terminal中输入python manage.py makemigrations，执行成功后就会在App的文件夹中的migrations文件夹中
            生成0001_initial.py，在里面包含数据库的操作日志

    第三步：进行数据的同步：
        在pycharm的Terminal中输入python manage.py migrate，执行成功后打开数据库，就会看见很多数据库表，这样就完成
            了功能的注册和数据表的同步
'''

