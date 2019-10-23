from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Article
# Create your views here.
def test(request):
    return HttpResponse('你好')
def article(request):
    if request.method=='GET' and request.GET:
        id = int(request.GET.get('id'))
        test = Article.objects.get(id = id)
    return render_to_response('article.html',{'article':test})

from pure_pagination import Paginator,PageNotAnInteger

def articleList(request):
    articles = Article.objects.all()
    try:
        page = request.GET.get('page',1)
    except PageNotAnInteger:
        page = 1
    paginator = Paginator(articles,2)

    pageData = paginator.page(page)
    result = {
        'pageData':pageData
    }

    return render_to_response('articleList.html',result)