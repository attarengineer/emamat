from django.shortcuts import render


def blog_view(request):
    return render(request, '../templates/blog/blog.html')
