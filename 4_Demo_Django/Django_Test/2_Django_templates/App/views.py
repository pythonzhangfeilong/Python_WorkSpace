from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.template import Context

# 正常的写法
# def index(request):
#     return render(request,'index.html')

# def get_page(request):
#     template=get_template('index.html')
#     context=({})
#     return HttpResponse(template.render(context))

# def get_page(request):
# #获取模板
#     template = get_template('index.html')
# #处理上下文，主要做数据的交互
#     context = {}
# #前端响应展示
#     return HttpResponse(template.render(context))

# 变量
class Teacher():
    def teacher(self):
        return 'knowledge'

def get_page(self):
    template=get_template('index.html')
    context={
        'name':'for',
        'age':23,
        'project':['python','linux','html'],
        'company': {"name": "xuegod", "position": "beijing"},
        'method': Teacher()
    }

    return HttpResponse(template.render(context))

# for循环标签
from django.http import HttpResponse
from django.template.loader import get_template

News = [
    {"title": "for's editor", "author": "for", "time": "2018-06-13"},
    {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
    {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
    {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
    {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
    {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
]
def news(request):
    context = {"news": News}
    template = get_template("news.html")
    result = template.render(context)
    return HttpResponse(result)

# 嵌套for循环标签
News = [
    {"title": "For's editor","author": "for","time": "2018-06-13"},
    {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
    {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
    {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
    {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
    {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
]

def  news(request):
    context = {"news":News,"inner":[1,2,3]}
    template = get_template("news.html")
    result = template.render(context)
    return HttpResponse(result)

# forloop
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
#
# def navigation(request):
#     template = get_template("navigation.html")
#     context = {"data":Navigation}
#     result = template.render(context)
#     return HttpResponse(result)

# forloop的嵌套
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
#
# def navigation(request):
#     template = get_template("navigation.html")
#     context = {"data":Navigation,"inner":[1,2,3]}
#     result = template.render(context)
#     return HttpResponse(result)

# 过滤器调用的方法
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
    template = get_template("navigation.html")
    context = {"data":Navigation,"inner":[1,2,3]}
    result = template.render(context)
    return HttpResponse(result)
