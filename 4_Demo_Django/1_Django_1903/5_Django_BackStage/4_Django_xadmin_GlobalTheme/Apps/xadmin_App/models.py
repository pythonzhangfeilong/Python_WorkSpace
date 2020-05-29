from django.db import models

# 案例
class Example(models.Model):
    name=models.CharField(max_length=32,verbose_name='作者')
    type=models.CharField(max_length=32,verbose_name='分类')

    class Mate:
        verbose_name='案例'
        verbose_name_plural=verbose_name
    
    def __str__(self):
        return '作者：%s'%self.name

#作者
class Author(models.Model):
    gender_choice = (
        ('M','Male'),
        ('F','Female'),
    )
    name = models.CharField(max_length=32,verbose_name='作者姓名')
    age = models.IntegerField(verbose_name='作者年龄',blank=True,null=True)
    gender = models.CharField(max_length=2,choices=gender_choice,verbose_name='作者姓名',blank=True,null=True)
    email = models.EmailField(verbose_name='作者邮箱',blank=True,null=True)
    phone = models.CharField(max_length=11,verbose_name='作者电话',blank=True,null=True)
    #在admin下展示这个表的中文名字
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
    # isdelete = models.IntegerField
    def __str__(self):
        return '作者:%s'%self.name
#分类
class Classify(models.Model):
    label = models.CharField(max_length=32,verbose_name='分类标签')
    description = models.TextField(verbose_name='分类描述')

    class Meta:
        verbose_name='分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '标签:%s'%self.label

from ckeditor_uploader.fields import RichTextUploadingField

#文章
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='文章标题')
    time = models.DateField(verbose_name='文章发表日期')
    description = RichTextUploadingField(verbose_name='文章描述')
    content = RichTextUploadingField(verbose_name='文章内容')
    #外键关联（一对多关系……）
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    # isdelete =
    #多对多关系
    classify = models.ManyToManyField(Classify)

    picture = models.ImageField(upload_to='images/%Y%m',default='image/default.png',verbose_name='文章图片')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '文章:%s'%self.title