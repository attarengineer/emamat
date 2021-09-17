from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_archive_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, '../templates/blog/blog-archive.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, '../templates/blog/blog-single.html', context)
