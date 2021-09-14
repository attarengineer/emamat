from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, '../templates/website/index.html')


def about_view(request):
    return render(request, '../templates/website/about.html')


def contact_view(request):
    return render(request, '../templates/website/contact.html')


def http_test(request):
    return HttpResponse('<h1>salam bacheha</h1>')


def json_test(request):
    return JsonResponse({'name': 'alireza'})



