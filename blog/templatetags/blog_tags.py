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


@register.inclusion_tag('blog/blog-slider.html')
def slider(arg=5, cat=3):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-new.html')
def latest_news(arg=20):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-sidebar-box-top.html')
def sidebar_box_top(arg=1, cat=3):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-sidebar-box-down.html')
def sidebar_box_down(arg=3, cat=3):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[1:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-sidebar-slider.html')
def sidebar_slider(arg=3, cat=3):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-footer.html')
def blog_footer(arg=5, cat=3):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-single-similar-post.html')
def blog_similar_post(arg=4, cat=1):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-map-city.html')
def blog_map_city(arg=4, cat=1):
    posts = Post.objects.filter(status=1, category=cat).order_by('-published_date')[:arg]
    return {'posts': posts}
