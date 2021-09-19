from django.contrib import admin
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title',)
    list_display = ('title', 'author', 'counter_views', 'status', 'created_date')
    list_filter = ('status', 'author')
    ordering = ['-created_date']
    search_fields = ['title', 'content']


@admin.register(Category)
class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'id')