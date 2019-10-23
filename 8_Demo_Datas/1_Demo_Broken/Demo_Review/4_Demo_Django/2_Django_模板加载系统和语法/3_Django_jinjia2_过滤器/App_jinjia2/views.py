from django.shortcuts import render

def func_jinjia(request):
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
    return render(request,'index.html',context={'nav':Navigation})
