from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('links', links_view, name='links'),
    path('api/<str:state>', api_view, name='api'),
    path('api/', api_view, name='api'),
]
