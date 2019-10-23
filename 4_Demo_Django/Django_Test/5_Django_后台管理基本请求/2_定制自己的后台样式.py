#####定制自己的后台样式
'''
    1、样式类定义
        添加样式需要定义样式类
            list_display = ('id','Name',)     --列表中显示的列
            search_fields = ('id', 'Name')   --搜索框
            list_filter = ('Name',)              --侧边过滤器
            date_hierarchy = 'DataTime3'  --时间下拉
            ordering = ('-DataTime3',)      --列表中的排序
            fields = ('Name','DataTime1')  --详细页面字段顺序
            filter_horizontal = ('Name',)    --显示多对多的关系
            raw_id_fields = ('publisher',)   --显示外键的数据
        在App文件夹中找到admin.py文件，写入：前提是在models.py中有Exaple
            from .models import Exaple
            @admin.register(Exaple)
            class ExapleAdmin(admin.ModelAdmin):
                list_display = ('name','type')
                search_fields = ('name','type')
                list_filter = ('name','type')
        在浏览器访问地址：http://127.0.0.1:8000/admin/   点击Users，就会看到新添加的内容
'''