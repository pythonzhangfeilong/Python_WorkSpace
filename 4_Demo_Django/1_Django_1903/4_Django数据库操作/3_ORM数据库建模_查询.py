##### ORM数据库建模_查询
'''
    ORM查询之前需要俩个魔法方法是：
        __str__     当类当中设定了__str__之后，凡是要打印类的实例，都会返回指定的这个字符串
        __repr__    而repr会更加的彻底，实例之间返回名称
'''

'''
    1、首先在App文件夹中的models.py文件中插入：
        def __str__(self):
            return self.name
    完成上面的操作，就是完成了数据模型的定义和同步
'''

#####Django数据库ORM的操作：增删查改
'''
    这个数据库操作实在shell模式下进行，在pycharm的Terminal中输入pip install ipython安装ipython，安装完成后输入
        python manage.py shell
'''

# 增
'''
使用实例化的方法：
    在pycharm的Terminal下输入:
    python manage.py shell
    from ORM_App.models import Exaple
    e=Exaple()
    e.name='zhang'
    e.type='Python'
    e.save()
    pycharm连接orm_django_exaple就可以查看到数据
    
在pycharm的Terminal下使用Model.objects.create()语句对字段进行赋值，可以实现一句话保存数据：
    e=Exaple.objects.create(name='fei',type='Linux')
    pycharm连接orm_django_exaple就可以查看到数据
    
'''

# 查
'''
查看所有的数据：e=Exaple.objects.all()
    解释：数据库的名字也就是类名点上后面的固定格式
按条件查询数据：e=Exaple.objects.filter(name='zhang')
    解释：数据库的名字也就是类名点上后面的固定格式，括号中的内容是根据查询字段的内容
多条件查询：e=Exaple.objects.filter(name='zhang',type='Python')
    解释：数据库的名字也就是类名点上后面的固定格式，括号中的内容是根据查询字段的内容
条件模糊查询：e=Exaple.objects.filter(type__contians='p')
    解释：数据库的名字也就是类名点上后面的固定格式，括号中的内容是根据查询字段的内容
    
    多条件模糊查询其他关键字：
        __exact 精确等于 like ‘aaa’ 
        __iexact 精确等于 忽略大小写 ilike ‘aaa’ 
        __contains 包含 like ‘%aaa%’ 
        __icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。 
        __gt 大于 
        __gte 大于等于 
        __lt 小于 
        __lte 小于等于 
        __in 存在于一个list范围内 
        __startswith 以…开头 
        __istartswith 以…开头 忽略大小写 
        __endswith 以…结尾 
        __iendswith 以…结尾，忽略大小写 
        __range 在…范围内 
        __year 日期字段的年份 
        __month 日期字段的月份 
        __day 日期字段的日 
        __isnull=True/False 
        __isnull=True 与 __exact=None的区别
查一条数据：e=Exaple.objects.get(name='zhang')
排序查：e=Exaple.objects.order_by('name')
截取查：e=Exaple.objects.all()[:3]
混合查：e=Exaple.objects.order_by('name').get(id=1)
'''

# 删除只有一个方法delete
'''
    删除之前先要e=Exaple.objects.order_by('name').get(id=1)或者其他条件查出来
    然后e.delete()
'''

# 改
'''
修改单个数据的时候，是需要e=Exaple.objects.order_by('name').get(id=1)或者其他条件查出来
然后e.name
写上新的值

修改多条数据的时候是需要update实现
    e=Exaple.objects.filter(type__contians='p').update(type='PYTHON')
'''















