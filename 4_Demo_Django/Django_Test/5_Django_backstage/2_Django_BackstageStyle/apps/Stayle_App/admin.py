from django.contrib import admin

from .models import Exaple
@admin.register(Exaple)
class ExapleAdmin(admin.ModelAdmin):
    list_display = ('name','type')
    search_fields = ('name','type')
    list_filter = ('name','type')