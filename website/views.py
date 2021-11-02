from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm
from django.contrib import messages
from django.conf import settings
from jalali_date import datetime2jalali, date2jalali

def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'پیام شما با موفقیت ارسال شد.')
        else:
            messages.add_message(request, messages.ERROR, 'ارسال پیام با خطا مواجه شد.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form, 'site_key': site_key})


def links_view(request):
    return render(request, 'website/links.html')


def api_view(request, state):
    data = Post.objects.filter(status=1, state__name=state)
    posts = []
    for post in data:
        item = {
            'id': post.id,
            'title': post.title,
            'image': post.image.url,
            'publisheddate': datetime2jalali(post.published_date).strftime('%y/%m/%d _ %H:%M:%S')
        }
        posts.append(item)
    return JsonResponse({'posts': posts[:2]})
