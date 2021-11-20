from django.contrib import admin
from .models import *
# Register your models here.

class MessageContactAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','email','seen']

    class Meta:
        model = MessageContact

admin.site.register(MessageContact,MessageContactAdmin)