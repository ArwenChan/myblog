from django.contrib import admin
from .models import Blog, Tags
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blog_type', 'creat_date', 'reads', 'likes')
    list_filter = ['creat_date']
    search_fields = ['name']


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
