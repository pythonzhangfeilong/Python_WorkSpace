#####ORM数据库建模：
'''
    数据库建模就是在设计数据库时，对现实世界进行分析、抽象、并从中找出内在联系，确定数据库的结构，这一过程就称为数据库建模。
    它主要包括两部分内容：
        确定最基本的数据结构；对约束建模。
    在这里需要注意的两个点：
        对业务实体的描述
        对业务实体间关系的描述
'''

#####ORM数据库建模：
'''
    1、首先数据库建模需要对业务逻辑进行分析和规划（特别重要）
    2、然后分析描述数据库
    
    Django中描述数据库如下：
        类名       对应     表名
        类变量     对应     字段名
    
    在App的models.py文件中写入:
        from django.db import models
        class Exaple(models.Model):
            # 创建表的时候一定要注意后面不能加逗号
            name=models.CharField(max_length=32,verbose_name='案例的名称')
            type=models.CharField(max_length=32,verbose_name='案例的类型')
        需要注意的内容：
            Django的项目的类的名称首字母必须大写
            Django的模型的类必须继承models.Model   
            Django模型的models类当中有定义好的字段类型
            
    在App的views.py文件中写入：
        from django.shortcuts import render
from work_App import models
def func(request):
    # 注意POST一定要大写
    if request.method=='POST':
        # get括号里面的字体内容要与HTML中标签里name一致
        First_Name = request.POST.get('First Name')
        Last_Name = request.POST.get('Last Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password =request.POST.get('Confirm Password')
        # 在服务器中输出提交的内容，也可以不写
        print(First_Name,Last_Name,Email,Password,Confirm_Password)
        models.UserData.objects.create(
        # Models.py中的变量名=views.py中的变量名
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email=Email,
            Password=Password,
            Confirm_Password=Confirm_Password,
        )
    return render(request,'index.html')
    
    # 还要注意在html中form表单的action后面跟的是页面响应ur的名称
'''

#####ORM创建数据库常用字段：
'''
1、models.AutoField　　		自增列 = int(11)如果没有的话，默认会生成一个名称为 id 的列，如果要显示的自定义一个自增列，必须将给列设置为主键 primary_key=True。
2、models.CharField　　		字符串字段，必须 max_length 参数
3、models.BooleanField　　		布尔类型=tinyint(1)，不能为空，Blank=True
4、models.ComaSeparatedIntegerField　　用逗号分割的数字=varchar继承CharField，所以必须 max_lenght 参数
5、models.DateField　　		日期类型 date对于参数，auto_now = True 则每次更新都会更新这个时间；auto_now_add 则只是第一次创建添加，之后的更新不再改变。
6、models.DateTimeField　		日期类型 datetime 同DateField的参数
7、models.Decimal　　			十进制小数类型 = decimal必须指定整数位max_digits和小数位decimal_places
8、models.EmailField　　		字符串类型（正则表达式邮箱） =varchar对字符串进行正则表达式
10、models.FloatField　　		浮点类型 = double
10、models.IntegerField　　		整形
11、models.BigIntegerField　　	长整形
    integer_field_ranges = {
    　　　　					'SmallIntegerField': (-32768, 32767),
    　　　　					'IntegerField': (-2147483648, 2147483647),
    'BigIntegerField': (-10223372036854775808, 10223372036854775807),
    　　　　					'PositiveSmallIntegerField': (0, 32767),
    　　　　					'PositiveIntegerField': (0, 2147483647),
    　　					}
12、models.IPAddressField　　			字符串类型（ip4正则表达式）
13、models.GenericIPAddressField　　	字符串类型（ip4和ip6是可选的）参数protocol可以是：both、ipv4、ipv6，验证时，会根据设置报错
14、models.NullBooleanField　　		允许为空的布尔类型
15、models.PositiveIntegerFiel　　		正Integer
16、models.PositiveSmallIntegerField　　	正smallInteger
17、models.SlugField　　				减号、下划线、字母、数字
18、models.SmallIntegerField　　		数字数据库中的字段有：tinyint、smallint、int、bigint
19、models.TextField　　			字符串=longtext
20、models.TimeField　　			时间 HH:MM[:ss[.uuuuuu]]
21、models.URLField　　			字符串，地址正则表达式
22、models.BinaryField　　			二进制
23、models.ImageField  			图片
24、models.FilePathField 			文件
'''

#####ORM创建数据库常用字段参数：
'''
1、null=True						数据库中字段是否可以为空
2、blank=True		 			django的 Admin 中添加数据时是否可允许空值
3、primary_key = False 			主键，对AutoField设置主键后，就会代替原来的自增 id 列
4、auto_now 和 auto_now_add
　　auto_now   					自动创建---无论添加或修改，都是当前操作的时间
　　auto_now_add  				自动创建---永远是创建时的时间
5、choices
    GENDER_CHOICE = (
            (u'M', u'Male'),
            (u'F', u'Female'),
        )
    gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
6、max_length
7、default　　				默认值
8、verbose_name　　		Admin中字段的显示名称
10、name|db_column　　	数据库中的字段名称
10、unique=True　　		不允许重复
11、db_index = True　　	数据库索引
12、editable=True　　		在Admin里是否可编辑
13、error_messages=None　错误提示
14、auto_created=False　　	自动创建
15、help_text　　			在Admin中提示帮助信息
16、validators=[]
17、upload-to   			上传到哪个位置,更多与image,filepath配合使用
18、on_delete  			例如on_delete = models.CASCADE, # 删除关联数据,与之关联也删除 。注意：老版本django不写没事，新版本不写会出现错误（外键关联中）
'''



