import xadmin
from .models import Author,Article,Classify,Example

class AuthorAdmin(object):
    list_display = ['name','age','gender','email','phone']
    search_fields = ['name','age','gender','email','phone']
    list_filter = ['name','age','gender','email','phone']

class ExampleAdmin(object):
    list_display = ['name','type']
    search_fields = ['name','type']
    list_filter = ['name','type']

class ArticleAdmin(object):
    list_display = ['title','time','description','content','author','classify']
    search_fields = ['title','time','description','content','author','classify']
    list_filter = ['title','time','description','content','author','classify']

class ClassifyAdmin(object):
    list_display = ['label','description']
    search_fields = ['label','description']
    list_filter = ['label','description']

# xadmin.site.register(Example,ExampleAdmin)
xadmin.site.register(Author,AuthorAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Classify,ClassifyAdmin)

