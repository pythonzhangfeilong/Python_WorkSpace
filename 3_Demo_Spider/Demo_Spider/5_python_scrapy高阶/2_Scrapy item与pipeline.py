# 1、items.py            是定义scrapy内部数据的文件，
# 2、pipelines.py        当items返回的时候，会自动的调用pipelines类中的process_item()，需要添加到settings.py里面

# scrapy有一个巨大的优势，scrapy可以定义数据模型，items可以定义数据模型，定义的方法类似django的模型

# scrapy会默认创建一个模型，可以在里卖弄定义想要的数据模型
'''
    1、scrapy的items中左右的字段都可以为Field
    2、scrapy当中定义模型是一个类，是类就要遵守python的语法规则
'''



















