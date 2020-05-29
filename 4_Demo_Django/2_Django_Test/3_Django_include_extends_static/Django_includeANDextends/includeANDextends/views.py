from django.shortcuts import render

from django.shortcuts import render_to_response
def framework_page(request):
    return render_to_response('framework.html')

def extends_base(request):
    return render_to_response('extends_base.html')





