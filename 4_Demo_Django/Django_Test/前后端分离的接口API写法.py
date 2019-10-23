from .models import  Article
from pure_pagination import Paginator
from django.http import JsonResponse


def vuetest(request):
    """
    提供分页的ajax数据
    """
    if request.method == "GET": #如果是get请求
        try:
            page = request.GET.get('page',1)
        except:
            page = 1
        aritcles = Article.objects.all() #查询所有的数据
        paginator = Paginator(aritcles,2) #对数据进行分页，每页三条
        pageData = paginator.page(page) #获取具体页的数据
        print(pageData)
        page_data = [] #对数据进行json结构化，json只接受字典对象[{},{}]
        for data in pageData.object_list:
            classify = data.classify.all() #多对多字段需要首先查询出所有对应的字段,查询出来还是数据库对象
            if classify:
                classify = [i.label for i in classify] #对字段取指定的lable
            else:
                classify = "" #空类表不可以建json序列，所以，我们改完字符串
            page_data.append(
                {
                    "title": data.title,
                    "author": data.author.name, #w外键，必须调用具体的字段
                    "time": data.time,
                    "description": data.description,
                    "picture": data.picture.name, #这里的name是由于文件对象有name属性
                    "classify": classify,
                    "id": data.id
                }
            )
        result = {
            "pageData": page_data
        }
        return JsonResponse(result)
