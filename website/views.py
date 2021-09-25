from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm
from django.contrib import messages


def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'پیام شما با موفقیت ارسال شد.')
        else:
            messages.add_message(request, messages.ERROR, 'ارسال پیام با خطا مواجه شد.')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})





