from django.template.loader import get_template
from django.shortcuts import HttpResponse

def get_page(request):
    template = get_template('HTML/index.html')
    context = (
        {'name':'for',
         'age':23,
         'project':['python','linux','html'],
         'company': {"name": "xuegod", "position": "beijing"},
         }
    )
    return HttpResponse(template.render(context))
