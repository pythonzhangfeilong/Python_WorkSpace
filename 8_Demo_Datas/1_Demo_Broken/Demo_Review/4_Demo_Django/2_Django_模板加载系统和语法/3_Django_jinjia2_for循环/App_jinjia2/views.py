from django.shortcuts import render

def func_jinjia(request):
    News=[
        {"title": "for's editor", "author": "for", "time": "2018-06-13"},
        {"title": "MK's editor", "author": "MK", "time": "2018-06-13"},
        {"title": "CD's editor", "author": "CD", "time": "2018-06-13"},
        {"title": "RM's editor", "author": "RM", "time": "2018-06-13"},
        {"title": "Django's editor", "author": "Django", "time": "2018-06-13"},
        {"title": "Twisted's editor", "author": "Twisted", "time": "2018-06-13"}
    ]
    # 注意上下文的传递context必须是字典
    return render(request,'index.html',context={'news':News})