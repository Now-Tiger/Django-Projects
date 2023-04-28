from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.register(Todo)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug' : ('title', )}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')