from django import template
from blog.models import Post, Category


register = template.Library()


@register.inclusion_tag('blog/blog-last-post-archive.html')
def lastpost_archive(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-last-post-single.html')
def lastpost_single(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-filter-posts.html')
def filter_posts(arg=3, cat=1):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-header.html')
def filter_post_header(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcatgories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
