from django.contrib import admin
from website.models import Contact


@admin.register(Contact)
class ContactAdmin (admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'email', 'subject']
    fields = ('name', 'email', 'subject', 'message', 'created_date', 'update_date')
    readonly_fields = ['created_date', 'update_date']
