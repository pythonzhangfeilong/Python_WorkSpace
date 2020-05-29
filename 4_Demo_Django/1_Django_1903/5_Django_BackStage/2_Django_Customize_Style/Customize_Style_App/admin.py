from django.contrib import admin
from Customize_Style_App.models import Example
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('name','type')
    search_fields = ('name','type')
    list_filter = ('name','type')