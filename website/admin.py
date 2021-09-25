from django.contrib import admin
from website.models import Contact


@admin.register(Contact)
class ContactAdmin (admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
