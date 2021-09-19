from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag('blog/blog-last-post-archive.html')
def lastpost_archive(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-last-post-single.html')
def lastpost_single(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}
