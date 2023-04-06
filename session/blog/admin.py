from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)