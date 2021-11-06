from django.contrib import admin
from blog.models import Post, Category, State
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin (SummernoteModelAdmin):
    summernote_fields = 'content'
    date_hierarchy = 'created_date'
    # fields = ('title',)
    list_display = ('title', 'counter_views', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    # ordering = ['-published_date']
    search_fields = ['title', 'content']


@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(State)
class StateAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')
