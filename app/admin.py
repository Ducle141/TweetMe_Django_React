# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user_username', 'user_email']
    class Meta:
        model = Tweet


admin.site.register(Tweet)