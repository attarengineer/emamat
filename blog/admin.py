from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # fields = ('title',)
    list_display = ('title', 'counter_views', 'status', 'created_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title', 'content']