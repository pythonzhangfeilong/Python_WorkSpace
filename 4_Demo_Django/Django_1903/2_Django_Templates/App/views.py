from django.shortcuts import render
from django.shortcuts import HttpResponse

##### 模板加载
# def index(request):
#     return render(request,'index.html')

##### 1、{{  }} 以双大括号包围的 变量
# class Teacher():
#     def teacher(self):
#         return 'This is class Teacher'
# def get_page(request):
#     context={
#         'name':'zhang',
#         'age':23,
#         'project':['Python','Linux','Java'],
#         'company':{'name':'Python','address':'huhehaote'},
#         # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
#         # {{methde.teacher}}
#         'methde':Teacher()
#     }
#     return render(request,'index.html',context=context)

##### 2、{%  %} 以大括号和%号包围的  标签语句
# if语句
# class Teacher():
#     def teacher(self):
#         return 'This is class Teacher'
# def get_page(request):
#     context={
#         'name':'zhang',
#         'age':23,
#         'project':['Python','Linux','Java'],
#         'company':{'name':'Python','address':'huhehaote'},
#         # 下面的这个就像与是一个将类实例化对象的一个操作，在html中按照下面的这种写法就可以调用到类中的函数
#         # {{methde.teacher}}
#         'methde':Teacher()
#     }
#     return render(request,'index.html',context=context)


# for循环
# News = [
#     {"title": "for's editor","author": "for","time": "2018-06-13"},
#     {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
#     {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
#     {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
#     {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
#     {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
# ]
# def news(request):
#     context={'news':News}
#     return render(request, 'for.html', context=context)

# 嵌套for循环
# News = [
#     {"title": "for's editor","author": "for","time": "2018-06-13"},
#     {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
#     {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
#     {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
#     {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
#     {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
# ]
# def news(request):
#     context={'news':News,'inner':[1,2,3]}
#     return render(request, 'for.html', context=context)

# forloop       （查看for循环的位置）
# Navigation = [
#     {"id": 1, "label": "python", "href": "python", "parent_id": 0},
#     {"id": 2, "label": "java", "href": "python", "parent_id": 0},
#     {"id": 3, "label": "php", "href": "python", "parent_id": 0},
#     {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
#     {"id": 5, "label": "django", "href": "python", "parent_id": 1},
#     {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
#     {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
#     {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
#     {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
# ]
# def forloop(request):
#     context={'data':Navigation}
#     return render(request,'forloop.html',context=context)

# 嵌套forloop       （查看for循环的位置）
# Navigation = [
#     {"id": 1, "label": "python", "href": "python", "parent_id": 0},
#     {"id": 2, "label": "java", "href": "python", "parent_id": 0},
#     {"id": 3, "label": "php", "href": "python", "parent_id": 0},
#     {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
#     {"id": 5, "label": "django", "href": "python", "parent_id": 1},
#     {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
#     {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
#     {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
#     {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
# ]
# def forloop(request):
#     context={'data':Navigation,'inner':[1,2,3]}
#     return render(request,'forloop.html',context=context)

##### |  用于变量后进行修饰的过滤器
Navigation = [
    {"id": 1, "label": "python", "href": "python", "parent_id": 0},
    {"id": 2, "label": "java", "href": "python", "parent_id": 0},
    {"id": 3, "label": "php", "href": "python", "parent_id": 0},
    {"id": 4, "label": ".net", "href": "python", "parent_id": 0},
    {"id": 5, "label": "django", "href": "python", "parent_id": 1},
    {"id": 6, "label": "flask", "href": "python", "parent_id": 1},
    {"id": 8, "label": "spring", "href": "python", "parent_id": 2},
    {"id": 8, "label": "xadmin", "href": "python", "parent_id": 5},
    {"id": 9, "label": "django_ckeditor", "href": "python", "parent_id": 5},
    ]
def navigation(request):
    context={'navigation':Navigation}
    return render(request,'modification.html',context=context)








