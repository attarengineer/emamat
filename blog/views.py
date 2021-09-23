from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_archive_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = Post.objects.filter(status=1, category__name=cat_name)
    if author_username:
        posts = Post.objects.filter(status=1, author__username=author_username)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-archive.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-archive.html', context)
