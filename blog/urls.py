from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_archive_view, name='blog-archive'),
    path('<int:pid>', blog_single_view, name='blog-single'),
    path('category/<str:cat_name>', blog_archive_view, name='category'),
    path('author/<str:author_username>', blog_archive_view, name='author'),
    path('search/', blog_search, name='search')
]
