from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title',)
    list_display = ('title', 'author', 'counter_views', 'status', 'created_date', 'published_date')
    list_filter = ('status', 'author')
    # ordering = ['-published_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')
