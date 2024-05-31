from django.contrib import admin
from pages.models import FormContactModel
# Register your models here.
@admin.register(FormContactModel)
class FormContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')
    
    