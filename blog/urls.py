from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_archive_view, name='blog-archive'),
    path('<int:pid>', blog_single_view, name='blog-single'),
]
