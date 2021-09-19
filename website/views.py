from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, JsonResponse


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, '../templates/website/index.html', context)


def about_view(request):
    return render(request, '../templates/website/about.html')


def contact_view(request):
    return render(request, '../templates/website/contact.html')


def http_test(request):
    return HttpResponse('<h1>salam bacheha</h1>')


def json_test(request):
    return JsonResponse({'name': 'alireza'})



