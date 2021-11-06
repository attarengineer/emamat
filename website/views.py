from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm
from django.contrib import messages
from django.conf import settings
from jalali_date import datetime2jalali, date2jalali
import datetime


def index_view(request):
    posts = Post.objects.filter(status=1)
    current_datetime = datetime.datetime.now()
    context = {'posts': posts, 'current_datetime': current_datetime}
    return render(request, 'website/index.html', context)


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    # site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'پیام شما با موفقیت ارسال شد.')
        else:
            messages.add_message(request, messages.ERROR, 'ارسال پیام با خطا مواجه شد.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def links_view(request):
    return render(request, 'website/links.html')


def api_view(request, **kwargs):
    if kwargs.get('state'):
        data = Post.objects.filter(status=1, state__name=kwargs['state'])
    elif request.is_ajax():
        pk = request.POST.get('pk')
        data = Post.objects.filter(pk=pk)

        for post in data:
            post.like += 1
            post.save()

    else:
        data = Post.objects.filter(status=1)
    posts = []
    for post in data:
        item = {
            'id': post.id,
            'title': post.title,
            'image': post.image.url,
            'like': post.like,
            'publisheddate': datetime2jalali(post.published_date).strftime('%y/%m/%d _ %H:%M:%S')
        }
        posts.append(item)
    if kwargs.get('state'):
        posts = posts[:2]
    return JsonResponse({'posts': posts})
